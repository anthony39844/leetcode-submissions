import os
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo
import requests

# --- Retrieve Configuration from GitHub Secrets ---
LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
CSRF_TOKEN = os.getenv("LEETCODE_CSRF_TOKEN")

if not LEETCODE_SESSION or not CSRF_TOKEN:
    print("Error: LEETCODE_SESSION or LEETCODE_CSRF_TOKEN is missing in environment variables.")
    sys.exit(1)

# --- Constants ---
BASE_URL = "https://leetcode.com/graphql/"
HEADERS = {
    "Content-Type": "application/json",
    "Cookie": f"csrftoken={CSRF_TOKEN}; LEETCODE_SESSION={LEETCODE_SESSION};",
    "X-CSRFToken": CSRF_TOKEN,
    "Referer": "https://leetcode.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

EXTENSIONS = {
    "bash": "sh",
    "c": "c",
    "cpp": "cpp",
    "csharp": "cs",
    "dart": "dart",
    "golang": "go",
    "java": "java",
    "javascript": "js",
    "kotlin": "kt",
    "mysql": "sql",
    "postgresql": "sql",
    "python": "py",
    "python3": "py",
    "ruby": "rb",
    "rust": "rs",
    "scala": "scala",
    "swift": "swift",
    "typescript": "ts",
}

# Timezone configurations
UTC_TZ = ZoneInfo("UTC")
CST_TZ = ZoneInfo("America/Chicago")


def get_all_accepted_submissions():
    """Paginate through all historical LeetCode submissions to fetch all accepted entries."""
    print("Starting collection of all accepted submissions...")
    all_accepted = []
    offset = 0
    limit = 20
    has_next = True

    query = """
    query ($offset: Int!, $limit: Int!) {
        submissionList(offset: $offset, limit: $limit) {
            hasNext
            submissions {
                id
                title
                titleSlug
                statusDisplay
                lang
                timestamp
            }
        }
    }
    """

    while has_next:
        print(f"Fetching offset {offset}...")
        variables = {"offset": offset, "limit": limit}
        try:
            response = requests.post(BASE_URL, json={"query": query, "variables": variables}, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            
            sub_list = data['data']['submissionList']
            submissions = sub_list['submissions']
            has_next = sub_list['hasNext']
            
            # Filter and store only accepted solutions
            accepted_batch = [s for s in submissions if s['statusDisplay'] == 'Accepted']
            all_accepted.extend(accepted_batch)
            
            offset += limit
            time.sleep(1)  # Mild rate-limiting guard rails
        except Exception as e:
            print(f"Error pagination failed at offset {offset}: {e}")
            break

    print(f"Completed fetching. Found {len(all_accepted)} total accepted submissions.")
    return all_accepted


def get_submission_details(submission_id):
    """Fetches submission source code, difficulty, and topic tags."""
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            question {
                questionId
                difficulty
                topicTags {
                    slug
                }
            }
        }
    }
    """
    variables = {"submissionId": int(submission_id)}
    response = requests.post(BASE_URL, json={"query": query, "variables": variables}, headers=HEADERS)
    return response.json()['data']['submissionDetails']


def get_cst_filename(unix_timestamp):
    """Converts a UTC timestamp to US Central Time (CST/CDT) and formats it as a 12-hour AM/PM filename."""
    utc_dt = datetime.fromtimestamp(int(unix_timestamp), tz=UTC_TZ)
    cst_dt = utc_dt.astimezone(CST_TZ)
    # %I is 12-hour hour (01-12)
    # %p is AM/PM indicator
    return cst_dt.strftime("%Y-%m-%d_%I-%M-%S-%p")


def save_code_to_path(folder_path, filename, ext, code):
    """Saves solution content safely to disk."""
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"{filename}.{ext}")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code + "\n")


def sync_to_local():
    submissions = get_all_accepted_submissions()
    if not submissions:
        print("No accepted submissions found to sync.")
        return

    for sub in submissions:
        ext = EXTENSIONS.get(sub['lang'], "txt")
        filename = get_cst_filename(sub['timestamp'])
        
        # Look ahead calculation to check for existing duplicates across locations
        # We temporarily format folder path name just to check if it's already on disk.
        # This saves LeetCode API call quotas by verifying local status first.
        title_slug = sub['titleSlug']
        
        # We need the question details to construct the true folder paths. 
        # But we don't have the questionId yet without an API hit.
        # Optimization: Call details only if needed, or bypass check if not fetched before.
        print(f"Processing submission #{sub['id']} for {sub['title']}...")
        
        # Limit API calls to preserve quotas
        time.sleep(1.5)
        
        try:
            details = get_submission_details(sub['id'])
            if not details or 'code' not in details:
                continue
        except Exception as e:
            print(f"Failed to fetch details for submission {sub['id']}: {e}")
            continue

        question_data = details['question']
        qid_padded = str(question_data['questionId']).zfill(4)
        difficulty = question_data.get('difficulty', 'Unknown')
        tags = [tag['slug'] for tag in question_data.get('topicTags', []) if tag.get('slug')]
        question_folder_name = f"{qid_padded}-{title_slug}"

        # Setup destination folders
        difficulty_folder = os.path.join("solutions-difficulty", difficulty, question_folder_name)
        difficulty_file_path = os.path.join(difficulty_folder, f"{filename}.{ext}")

        # Check if we already have this submission saved in difficulty
        if os.path.exists(difficulty_file_path):
            print(f"  Skipping: Submission from {filename} already exists locally.")
            continue

        # Save to solutions-difficulty
        save_code_to_path(difficulty_folder, filename, ext, details['code'])
        print(f"  Saved to solutions-difficulty: {difficulty_file_path}")

        # Save to solutions-categories
        if tags:
            for tag in tags:
                category_folder = os.path.join("solutions-categories", tag, question_folder_name)
                save_code_to_path(category_folder, filename, ext, details['code'])
                print(f"  Saved to solutions-categories ({tag}): {filename}.{ext}")
        else:
            uncat_folder = os.path.join("solutions-categories", "uncategorized", question_folder_name)
            save_code_to_path(uncat_folder, filename, ext, details['code'])
            print(f"  Saved to solutions-categories (uncategorized): {filename}.{ext}")


if __name__ == "__main__":
    sync_to_local()
