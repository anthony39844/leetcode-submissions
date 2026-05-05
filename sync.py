import os
import requests
import time

# --- Configuration ---
SESSION = os.environ['LEETCODE_SESSION']
CSRF_TOKEN = os.environ['LEETCODE_CSRF_TOKEN']
USERNAME = "anthony39844" 
URL = "https://leetcode.com"
EXTENSIONS = {"python": "py", "python3": "py", "cpp": "cpp", "java": "java", "javascript": "js"}

def call_leetcode(query, variables):
    headers = {
        "Cookie": f"LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}",
        "X-CSRFToken": CSRF_TOKEN,
        "Referer": "https://leetcode.com",
        # Adding this prevents many bot-detection blocks
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    
    resp = requests.post(URL, json={'query': query, 'variables': variables}, headers=headers)
    
    # Check if the request was successful
    if resp.status_code != 200:
        print(f"Error {resp.status_code}: {resp.text}")
        raise Exception(f"LeetCode API returned status code {resp.status_code}")
    
    try:
        return resp.json()
    except Exception as e:
        # This will show us if it's returning HTML instead of JSON
        print("Failed to parse JSON. Response was:")
        print(resp.text)
        raise e
def get_all_submissions():
    all_subs, offset, limit = [], 0, 20
    while True:
        query = """
        query acSubmissions($username: String!, $limit: Int!, $offset: Int!) {
            recentAcSubmissionList(username: $username, limit: $limit, offset: $offset) {
                id, titleSlug, lang, title
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
unique_problems = {}

for sub in submissions:
    slug = sub['titleSlug']
    if slug not in unique_problems:
        diff, topic, content = get_problem_details(slug)
        unique_problems[slug] = {"title": sub['title'], "diff": diff, "topic": topic}
    else:
        diff, topic = unique_problems[slug]["diff"], unique_problems[slug]["topic"]

    folder_path = os.path.join(diff, topic, slug)
    os.makedirs(folder_path, exist_ok=True)
    
    # Save code
    ext = EXTENSIONS.get(sub['lang'], "txt")
    file_path = os.path.join(folder_path, f"solution_{sub['id']}.{ext}")
    if not os.path.exists(file_path):
        print(f"Syncing {slug}...")
        with open(file_path, "w") as f:
            f.write(get_submission_code(sub['id']))
        time.sleep(0.5)

    # Individual README
    readme_path = os.path.join(folder_path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# {sub['title']}\n\n**Difficulty:** {diff} | **Topic:** {topic}\n\n{content}")

# --- Generate Root README ---
with open("README.md", "w") as f:
    f.write(f"# LeetCode Solutions Library\n\n")
    f.write(f"Total Unique Problems Solved: **{len(unique_problems)}**\n\n")
    f.write("## Problems by Category\n\n")
    
    # Sort for a clean table
    for slug in sorted(unique_problems.keys()):
        p = unique_problems[slug]
        path = f"{p['diff']}/{p['topic']}/{slug}"
        f.write(f"- [{p['title']}]({path}) ({p['diff']})\n")

print("Sync complete!")
