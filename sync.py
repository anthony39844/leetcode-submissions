import os
import sys
import time
from datetime import datetime
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

def get_accepted_submissions(limit=20):
    """Fetches the most recent submissions with timestamps."""
    query = """
    query ($offset: Int!, $limit: Int!) {
        submissionList(offset: $offset, limit: $limit) {
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
    variables = {"offset": 0, "limit": limit}
    try:
        response = requests.post(BASE_URL, json={"query": query, "variables": variables}, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        subs = data['data']['submissionList']['submissions']
        return [s for s in subs if s['statusDisplay'] == 'Accepted']
    except Exception as e:
        print(f"Error fetching submission list: {e}")
        sys.exit(1)

def get_submission_details(submission_id):
    """Fetches code, questionId, difficulty, and topic tags."""
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

def save_code_to_path(folder_path, filename, ext, code):
    """Helper to safely create directories and write files."""
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"{filename}.{ext}")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code + "\n")
    print(f"  Saved: {file_path}")

def sync_to_local():
    print("Fetching submissions from LeetCode...")
    submissions = get_accepted_submissions()
    
    if not submissions:
        print("No accepted submissions found.")
        return

    for sub in submissions:
        print(f"Processing: {sub['title']}...")
        
        # Avoid hitting LeetCode rate limits
        time.sleep(1)
        
        # 1. Fetch submission code and metadata
        try:
            details = get_submission_details(sub['id'])
            if not details or 'code' not in details:
                continue
        except Exception as e:
            print(f"Failed to fetch details for submission {sub['id']}: {e}")
            continue

        # 2. Extract metadata
        question_data = details['question']
        qid_padded = str(question_data['questionId']).zfill(4)
        difficulty = question_data.get('difficulty', 'Unknown')
        tags = [tag['slug'] for tag in question_data.get('topicTags', []) if tag.get('slug')]
        
        # 3. Format Submission Timestamp to a safe filename: YYYY-MM-DD_HH-MM-SS
        submission_time = datetime.fromtimestamp(int(sub['timestamp']))
        filename = submission_time.strftime("%Y-%m-%d_%H-%M-%S")
        
        ext = EXTENSIONS.get(sub['lang'], "txt")
        question_folder_name = f"{qid_padded}-{sub['titleSlug']}"

        # 4. Save structured by Topic Tag (Falls back to Difficulty if no tags exist)
        if tags:
            for tag in tags:
                # Structure: solutions/topic_tags/tag-name/0001-two-sum/2026-05-05_22-58-35.py
                folder_path = os.path.join("solutions", tag, question_folder_name)
                save_code_to_path(folder_path, filename, ext, details['code'])
        else:
            # Fallback to solutions/uncategorized/0001-two-sum/...
            folder_path = os.path.join("solutions", "uncategorized", question_folder_name)
            save_code_to_path(folder_path, filename, ext, details['code'])

        # 5. Save structured strictly by Difficulty (Always saved here too for easy browsing)
        # Structure: solutions/difficulty/Easy/0001-two-sum/2026-05-05_22-58-35.py
        difficulty_path = os.path.join("solutions", "difficulty", difficulty, question_folder_name)
        save_code_to_path(difficulty_path, filename, ext, details['code'])

if __name__ == "__main__":
    sync_to_local()
