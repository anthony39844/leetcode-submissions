import os
import sys
import time
import shutil
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

# --- Dynamic Workspace Configuration ---
REQUIRED_FOLDERS = [
    {
        "name": "solutions",
        "has_dynamic_subfolder": False
    },
    {
        "name": "solutions-difficulty",
        "has_dynamic_subfolder": True  
    }
]


def get_cst_filename(unix_timestamp):
    """Converts a UTC timestamp to US Central Time (CST/CDT) and formats it as a 12-hour AM/PM filename."""
    utc_dt = datetime.fromtimestamp(int(unix_timestamp), tz=UTC_TZ)
    cst_dt = utc_dt.astimezone(CST_TZ)
    return cst_dt.strftime("%Y-%m-%d_%I-%M-%S-%p")


def check_file_exists_locally(title_slug, timestamp, lang):
    """Checks if a specific submission file already exists in ALL configured local folders."""
    filename = get_cst_filename(timestamp)
    ext = EXTENSIONS.get(lang, "txt")
    full_filename = f"{filename}.{ext}"

    for folder_config in REQUIRED_FOLDERS:
        root_folder = folder_config['name']
        file_found = False
        if os.path.exists(root_folder):
            for root, dirs, files in os.walk(root_folder):
                if full_filename in files and root.endswith(title_slug):
                    file_found = True
                    break
        if not file_found:
            return False
    return True


def get_all_accepted_submissions(stop_on_first_match=False):
    """Paginate through LeetCode submissions, stopping early the moment a match is found."""
    print("Starting collection of accepted submissions...")
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
            
            accepted_batch = [s for s in submissions if s['statusDisplay'] == 'Accepted']
            
            # --- SMART OVERLAP CHECK ---
            if stop_on_first_match:
                stop_pagination = False
                for sub in accepted_batch:
                    if check_file_exists_locally(sub['titleSlug'], sub['timestamp'], sub['lang']):
                        print(f"✨ Hit local historical boundary at '{get_cst_filename(sub['timestamp'])}'. Stopping pagination.")
                        stop_pagination = True
                        break
                
                if stop_pagination:
                    # Only grab the truly brand-new submissions from this batch before stopping
                    new_subs = []
                    for sub in accepted_batch:
                        if not check_file_exists_locally(sub['titleSlug'], sub['timestamp'], sub['lang']):
                            new_subs.append(sub)
                    all_accepted.extend(new_subs)
                    break

            # If no match was found in this batch, add them all and keep searching
            all_accepted.extend(accepted_batch)
            offset += limit
            time.sleep(1)  # Guard rail to prevent spamming LeetCode's gateway
        except Exception as e:
            print(f"Error: Pagination failed at offset {offset}: {e}")
            break

    print(f"Completed fetching. Identified {len(all_accepted)} unsynced submissions.")
    return all_accepted


def get_submission_details(submission_id):
    """Fetches submission source code and difficulty."""
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            question {
                questionId
                difficulty
            }
        }
    }
    """
    variables = {"submissionId": int(submission_id)}
    response = requests.post(BASE_URL, json={"query": query, "variables": variables}, headers=HEADERS)
    return response.json()['data']['submissionDetails']


def save_code_to_path(folder_path, filename, ext, code):
    """Saves solution content safely to disk."""
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"{filename}.{ext}")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code + "\n")


def sync_submission(sub):
    title_slug = sub['titleSlug']
    filename = get_cst_filename(sub['timestamp'])
    ext = EXTENSIONS.get(sub['lang'], "txt")
    full_filename = f"{filename}.{ext}"

    found_paths = {folder['name']: None for folder in REQUIRED_FOLDERS}

    # 1. Scan local directories to find copies
    for folder_config in REQUIRED_FOLDERS:
        root_folder = folder_config['name']
        if os.path.exists(root_folder):
            for root, dirs, files in os.walk(root_folder):
                if full_filename in files and root.endswith(title_slug):
                    found_paths[root_folder] = os.path.join(root, full_filename)
                    break

    missing_folders = [f for f in REQUIRED_FOLDERS if found_paths[f['name']] is None]
    found_folders = [f for f in REQUIRED_FOLDERS if found_paths[f['name']] is not None]

    # --- Case 1: Already fully synchronized ---
    if not missing_folders:
        return

    # --- Case 2: Local Copy Optimization (No API usage) ---
    if len(found_folders) > 0:
        print(f"  Optimizing: Local copy detected for '{full_filename}'. Bypassing API...")
        existing_path = found_paths[found_folders[0]['name']]
        path_parts = os.path.normpath(existing_path).split(os.sep)
        question_folder_name = path_parts[-2]

        for folder_config in missing_folders:
            dest_root = folder_config['name']
            if folder_config['has_dynamic_subfolder']:
                difficulty = sub.get('difficulty', 'Unknown')
                dest_folder = os.path.join(dest_root, difficulty, question_folder_name)
            else:
                dest_folder = os.path.join(dest_root, question_folder_name)
                
            os.makedirs(dest_folder, exist_ok=True)
            shutil.copy2(existing_path, os.path.join(dest_folder, full_filename))
            print(f"    -> Copied locally to: {dest_folder}")
        return

    # --- Case 3: API Fallback (Pull missing file from LeetCode) ---
    print(f"Processing submission #{sub['id']} for {sub['title']} (Calling API)...")
    time.sleep(1.5)  
    
    try:
        details = get_submission_details(sub['id'])
        if not details or 'code' not in details:
            return
    except Exception as e:
        print(f"Failed to fetch details for submission {sub['id']}: {e}")
        return

    question_data = details['question']
    qid_padded = str(question_data['questionId']).zfill(4)
    difficulty = question_data.get('difficulty', 'Unknown')
    question_folder_name = f"{qid_padded}-{title_slug}"

    for folder_config in REQUIRED_FOLDERS:
        dest_root = folder_config['name']
        if folder_config['has_dynamic_subfolder']:
            dest_folder = os.path.join(dest_root, difficulty, question_folder_name)
        else:
            dest_folder = os.path.join(dest_root, question_folder_name)
            
        save_code_to_path(dest_folder, filename, ext, details['code'])
        print(f"  Saved to {dest_root}: {full_filename}")


def generate_readme_stats():
    """Scans local folders and completely overwrites README.md with fresh progress stats."""
    print("Generating README statistics...")
    
    easy_count = 0
    medium_count = 0
    hard_count = 0

    # 1. Scan your directory structure to count unique problems solved
    diff_path = "solutions-difficulty"
    if os.path.exists(diff_path):
        for diff_level in ["Easy", "Medium", "Hard"]:
            level_folder = os.path.join(diff_path, diff_level)
            if os.path.exists(level_folder):
                # Count directories, which represent individual problems
                problems = [d for d in os.listdir(level_folder) if os.path.isdir(os.path.join(level_folder, d))]
                if diff_level == "Easy":
                    easy_count = len(problems)
                elif diff_level == "Medium":
                    medium_count = len(problems)
                elif diff_level == "Hard":
                    hard_count = len(problems)

    total_unique = easy_count + medium_count + hard_count

    # 2. Build the entire README content from scratch
    readme_content = f"""# LeetCode Submissions 🚀

My automated system for tracking solved LeetCode problems, categorized by difficulty.

### 📊 Progress Statistics

| Difficulty | Solved Count |
| :--- | :---: |
| 🟢 Easy | **{easy_count}** |
| 🟡 Medium | **{medium_count}** |
| 🔴 Hard | **{hard_count}** |
| **Total** | **{total_unique}** |

*Last updated: {datetime.now(CST_TZ).strftime('%Y-%m-%d %I:%M %p')} (Central Time)*

## 📂 Repository Structure

* **`solutions/`**: A flat directory containing all solved problems named by their completion timestamp.
* **`solutions-difficulty/`**: Solutions organized dynamically into `Easy`, `Medium`, and `Hard` folders.
"""

    # 3. Completely overwrite the file
    readme_file = "README.md"
    try:
        with open(readme_file, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print("README.md successfully regenerated with latest statistics!")
    except Exception as e:
        print(f"Error writing README.md: {e}")


def sync_to_local():
    # 1. Automatically detect if we need to do a full historical backfill.
    solutions_dir = "solutions"
    is_empty_repo = True
    
    if os.path.exists(solutions_dir):
        subfolders = [d for d in os.listdir(solutions_dir) if os.path.isdir(os.path.join(solutions_dir, d))]
        if len(subfolders) > 5:  
            is_empty_repo = False

    stop_on_first_match = not is_empty_repo
    
    if stop_on_first_match:
        print("🤖 Auto-detected existing repository. Running in fast Maintenance Mode.")
    else:
        print("🚀 Auto-detected empty or new repository. Running in full Backfill Mode.")

    # 2. Fetch submissions (with smart early-stopping boundary detection)
    submissions = get_all_accepted_submissions(stop_on_first_match=stop_on_first_match) 
    
    # 3. Process each submission
    for sub in submissions:
        sync_submission(sub)
        
    # 4. Regenerate README.md stats
    generate_readme_stats()


if __name__ == "__main__":
    sync_to_local()
