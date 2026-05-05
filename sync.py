import os
import requests
import time

# Secrets and Config
SESSION = os.environ['LEETCODE_SESSION']
CSRF_TOKEN = os.environ['LEETCODE_CSRF_TOKEN']
USERNAME = "your_username" 
URL = "https://leetcode.com/graphql"

EXTENSIONS = {"python": "py", "python3": "py", "cpp": "cpp", "java": "java", "javascript": "js"}

def call_leetcode(query, variables):
    headers = {
        "Cookie": f"LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}",
        "X-CSRFToken": CSRF_TOKEN,
        "Referer": "https://leetcode.com"
    }
    resp = requests.post(URL, json={'query': query, 'variables': variables}, headers=headers)
    return resp.json()

def get_all_submissions():
    """Fetches all accepted submissions using offset pagination."""
    all_subs = []
    offset = 0
    limit = 20
    while True:
        query = """
        query acSubmissions($username: String!, $limit: Int!, $offset: Int!) {
            recentAcSubmissionList(username: $username, limit: $limit, offset: $offset) {
                id
                titleSlug
                lang
                timestamp
            }
        }
        """
        data = call_leetcode(query, {"username": USERNAME, "limit": limit, "offset": offset})
        subs = data['data']['recentAcSubmissionList']
        if not subs: break
        all_subs.extend(subs)
        offset += limit
        time.sleep(1) # Prevent rate limiting
    return all_subs

def get_problem_info(title_slug):
    """Fetches difficulty and topic tags for a problem."""
    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            difficulty
            topicTags { name }
        }
    }
    """
    data = call_leetcode(query, {"titleSlug": title_slug})
    q = data['data']['question']
    topic = q['topicTags'][0]['name'] if q['topicTags'] else "General"
    return q['difficulty'], topic

def get_code(submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) { code }
    }
    """
    data = call_leetcode(query, {"submissionId": int(submission_id)})
    return data['data']['submissionDetails']['code']

# Main Execution
all_subs = get_all_submissions()

for sub in all_subs:
    diff, topic = get_problem_info(sub['titleSlug'])
    ext = EXTENSIONS.get(sub['lang'], "txt")
    
    # Path: Difficulty/Topic/ProblemName/SubmissionID.ext
    folder_path = os.path.join(diff, topic, sub['titleSlug'])
    os.makedirs(folder_path, exist_ok=True)
    
    file_path = os.path.join(folder_path, f"{sub['id']}.{ext}")
    
    if not os.path.exists(file_path):
        print(f"Syncing {sub['titleSlug']} (ID: {sub['id']})...")
        code = get_code(sub['id'])
        with open(file_path, "w") as f:
            f.write(code)
        time.sleep(0.5) # Avoid hitting API too hard
