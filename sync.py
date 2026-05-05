import os
import requests

# Secrets from GitHub
SESSION = os.environ['LEETCODE_SESSION']
CSRF_TOKEN = os.environ['LEETCODE_CSRF_TOKEN']
USERNAME = "anthony39844" # Hardcode it here since it's your personal repo

def fetch_submissions():
    url = "https://leetcode.com"
    headers = {
        "Cookie": f"LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}",
        "X-CSRFToken": CSRF_TOKEN,
        "Referer": "https://leetcode.com"
    }
    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
        recentAcSubmissionList(username: $username, limit: $limit) {
            title
            titleSlug
            timestamp
        }
    }
    """
    variables = {"username": USERNAME, "limit": 20}
    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    return response.json()['data']['recentAcSubmissionList']

submissions = fetch_submissions()

for sub in submissions:
    filename = f"{sub['titleSlug']}.txt"
    # Only create the file if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(f"Problem: {sub['title']}\nSolved on: {sub['timestamp']}")
        print(f"Added {filename}")
