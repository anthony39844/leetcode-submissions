import os
import requests

# Configuration
SESSION = os.environ['LEETCODE_SESSION']
CSRF_TOKEN = os.environ['LEETCODE_CSRF_TOKEN']
USERNAME = "your_username" 
URL = "https://leetcode.com/graphql"

# Map LeetCode language names to file extensions
EXTENSIONS = {
    "python": "py", "python3": "py", "cpp": "cpp", 
    "java": "java", "javascript": "js", "golang": "go"
}

def call_leetcode(query, variables):
    headers = {
        "Cookie": f"LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}",
        "X-CSRFToken": CSRF_TOKEN,
        "Referer": "https://leetcode.com"
    }
    response = requests.post(URL, json={'query': query, 'variables': variables}, headers=headers)
    return response.json()

def get_latest_submissions():
    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
        recentAcSubmissionList(username: $username, limit: $limit) {
            id
            titleSlug
            lang
        }
    }
    """
    data = call_leetcode(query, {"username": USERNAME, "limit": 10})
    return data['data']['recentAcSubmissionList']

def get_submission_code(submission_id):
    # This specific query fetches the actual source code
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
        }
    }
    """
    data = call_leetcode(query, {"submissionId": int(submission_id)})
    return data['data']['submissionDetails']['code']

# Main Execution
submissions = get_latest_submissions()

for sub in submissions:
    ext = EXTENSIONS.get(sub['lang'], "txt")
    filename = f"{sub['titleSlug']}.{ext}"
    
    if not os.path.exists(filename):
        print(f"Fetching code for: {sub['titleSlug']}...")
        code_content = get_submission_code(sub['id'])
        
        with open(filename, "w") as f:
            f.write(code_content)
        print(f"Saved {filename}")
