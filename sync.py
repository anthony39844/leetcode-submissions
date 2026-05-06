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
            print(f"Error: Pagination failed at offset {offset}: {e}")
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
        title_slug = sub['titleSlug']
        
        # We temporarily need to construct the folder name.
        # Since we don't have the question ID yet, we check the directory structure first.
        # However, to avoid calling the API, we can search if ANY directory ending with '-{title_slug}'
        # already contains our '{filename}.{ext}'. 
        
        already_exists = False
        # Fast local search to see if we already downloaded this exact file in any of our folders
        for root_folder in ["solutions", "solutions-difficulty"]:
            if os.path.exists(root_folder):
                for root, dirs, files in os.walk(root_folder):
                    if f"{filename}.{ext}" in files and root.endswith(title_slug):
                        already_exists = True
                        break
            if already_exists:
                break

        if already_exists:
            print(f"Skipping: Submission from {filename} for {sub['title']} already exists locally.")
            continue

        print(f"Processing submission #{sub['id']} for {sub['title']}...")
        time.sleep(1.5)  # Preserve API rate limit quotas
        
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

        # 1. Save to solutions (The new folder structure you requested)
        all_folder = os.path.join("solutions", question_folder_name)
        save_code_to_path(all_folder, filename, ext, details['code'])
        print(f"  Saved to solutions: {filename}.{ext}")

        # 2. Save to solutions-difficulty
        difficulty_folder = os.path.join("solutions-difficulty", difficulty, question_folder_name)
        save_code_to_path(difficulty_folder, filename, ext, details['code'])
        print(f"  Saved to solutions-difficulty: {filename}.{ext}")

        # 3. Save to solutions-categories
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
