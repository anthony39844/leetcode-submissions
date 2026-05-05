import os
import sys
import time
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
    "Referer": "https://leetcode.com"
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
    """Fetches the most recent submissions."""
    query = """
    query ($offset: Int!, $limit: Int!) {
        submissionList(offset: $offset, limit: $limit) {
            submissions {
                id
                title
                titleSlug
                statusDisplay
                lang
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
    """Fetches the actual code and question details for a submission."""
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            question {
                questionId
            }
        }
    }
    """
    variables = {"submissionId": int(submission_id)}
    response = requests.post(BASE_URL, json={"query": query, "variables": variables}, headers=HEADERS)
    return response.json()['data']['submissionDetails']

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
        
        # 1. Fetch submission code details
        try:
            details = get_submission_details(sub['id'])
            if not details or 'code' not in details:
                continue
        except Exception as e:
            print(f"Failed to fetch details for submission {sub['id']}: {e}")
            continue

        # 2. Structure folder path: "0001-two-sum"
        qid_padded = str(details['question']['questionId']).zfill(4)
        folder_name = f"{qid_padded}-{sub['titleSlug']}"
        os.makedirs(folder_name, exist_ok=True)
        
        # 3. Determine file extension
        ext = EXTENSIONS.get(sub['lang'], "txt")
        file_path = os.path.join(folder_name, f"solution.{ext}")
        
        # 4. Write the file to disk
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(details['code'] + "\n")
            
        print(f"Saved: {file_path}")

if __name__ == "__main__":
    sync_to_local()
