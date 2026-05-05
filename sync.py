import os
import requests
import time
import datetime

# --- Configuration ---
SESSION = os.environ['LEETCODE_SESSION']
CSRF_TOKEN = os.environ['LEETCODE_CSRF_TOKEN']
USERNAME = "your_username" 
URL = "https://leetcode.com"

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
    all_subs, offset, limit = [], 0, 20
    while True:
        query = """
        query acSubmissions($username: String!, $limit: Int!, $offset: Int!) {
            recentAcSubmissionList(username: $username, limit: $limit, offset: $offset) {
                id, titleSlug, lang, timestamp, title
            }
        }
        """
        data = call_leetcode(query, {"username": USERNAME, "limit": limit, "offset": offset})
        subs = data['data']['recentAcSubmissionList']
        if not subs: break
        all_subs.extend(subs)
        offset += limit
        time.sleep(0.5) 
    return all_subs

def get_problem_details(title_slug):
    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            content, difficulty, topicTags { name }
        }
    }
    """
    data = call_leetcode(query, {"titleSlug": title_slug})
    q = data['data']['question']
    topic = q['topicTags'][0]['name'] if q['topicTags'] else "General"
    return q['difficulty'], topic, q['content']

def get_submission_code(submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) { code }
    }
    """
    data = call_leetcode(query, {"submissionId": int(submission_id)})
    return data['data']['submissionDetails']['code']

# --- Main Logic ---
submissions = get_all_submissions()

for sub in submissions:
    diff, topic, content = get_problem_details(sub['titleSlug'])
    ext = EXTENSIONS.get(sub['lang'], "txt")
    
    # Path construction: Difficulty / Topic / Problem Name
    folder_path = os.path.join(diff, topic, sub['titleSlug'])
    os.makedirs(folder_path, exist_ok=True)
    
    # Save the solution file with ID to avoid overwriting
    file_path = os.path.join(folder_path, f"solution_{sub['id']}.{ext}")
    if not os.path.exists(file_path):
        print(f"Syncing {sub['titleSlug']} (ID: {sub['id']})...")
        code = get_submission_code(sub['id'])
        with open(file_path, "w") as f:
            f.write(code)
    
    # Generate/Update the README.md for this problem
    readme_path = os.path.join(folder_path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# {sub['title']}\n\n")
            f.write(f"**Difficulty:** {diff} | **Topic:** {topic}\n\n")
            f.write("## Problem Description\n")
            f.write(content + "\n\n")
            f.write("---")
