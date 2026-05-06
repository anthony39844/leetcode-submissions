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

# --- Dynamic Configuration ---
# Restructure your workspace simply by editing this list!
REQUIRED_FOLDERS = [
    {
        "name": "solutions",
        "has_dynamic_subfolder": False
    },
    {
        "name": "solutions-difficulty",
        "has_dynamic_subfolder": True  # Instructs the script to inject the difficulty subfolder
    }
]


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


def sync_submission(sub):
    title_slug = sub['titleSlug']
    
    # Correctly derive the filename using the raw 'timestamp' from the API payload
    filename = get_cst_filename(sub['timestamp'])
    ext = EXTENSIONS.get(sub['lang'], "txt")
    full_filename = f"{filename}.{ext}"

    # Track where the file is found during our local scan
    found_paths = {folder['name']: None for folder in REQUIRED_FOLDERS}

    # 1. Scan local directories dynamically based on REQUIRED_FOLDERS config
    for folder_config in REQUIRED_FOLDERS:
        root_folder = folder_config['name']
        if os.path.exists(root_folder):
            for root, dirs, files in os.walk(root_folder):
                # Ensure we match the exact filename inside the correct problem folder
                if full_filename in files and root.endswith(title_slug):
                    found_paths[root_folder] = os.path.join(root, full_filename)
                    break

    # Determine which folders are missing the file
    missing_folders = [f for f in REQUIRED_FOLDERS if found_paths[f['name']] is None]
    found_folders = [f for f in REQUIRED_FOLDERS if found_paths[f['name']] is not None]

    # --- Case 1: Already completely synced ---
    if not missing_folders:
        print(f"  Skipping: '{full_filename}' already exists in all configured folders.")
        return

    # --- Case 2: Local Copy Optimization (Found in at least one folder) ---
    if len(found_folders) > 0:
        print(f"  Optimizing: Local copy detected for '{full_filename}'. Bypassing API...")
        
        # Grab the path of any existing local copy
        existing_path = found_paths[found_folders[0]['name']]
        path_parts = os.path.normpath(existing_path).split(os.sep)
        question_folder_name = path_parts[-2]  # Extract e.g., "0001-two-sum"

        # Dynamically copy to all missing folders
        for folder_config in missing_folders:
            dest_root = folder_config['name']
            
            if folder_config['has_dynamic_subfolder']:
                # Dynamically construct the subfolder path using the submission's difficulty
                difficulty = sub.get('difficulty', 'Unknown')
                dest_folder = os.path.join(dest_root, difficulty, question_folder_name)
            else:
                dest_folder = os.path.join(dest_root, question_folder_name)
                
            os.makedirs(dest_folder, exist_ok=True)
            shutil.copy2(existing_path, os.path.join(dest_folder, full_filename))
            print(f"    -> Copied locally to: {dest_folder}")
        
        return

    # --- Case 3: API Fallback (Missing entirely) ---
    print(f"Processing submission #{sub['id']} for {sub['title']} (Calling API)...")
    
    # Respect rate limits
    time.sleep(1.5)  
    
    try:
        details = get_submission_details(sub['id'])
        if not details or 'code' not in details:
            return
    except Exception as e:
        print(f"Failed to fetch details for submission {sub['id']}: {e}")
        return

    # Gather required metadata from API response
    question_data = details['question']
    qid_padded = str(question_data['questionId']).zfill(4)
    difficulty = question_data.get('difficulty', 'Unknown')
    question_folder_name = f"{qid_padded}-{title_slug}"

    # Loop through REQUIRED_FOLDERS config dynamically to save the API data
    for folder_config in REQUIRED_FOLDERS:
        dest_root = folder_config['name']
        
        if folder_config['has_dynamic_subfolder']:
            dest_folder = os.path.join(dest_root, difficulty, question_folder_name)
        else:
            dest_folder = os.path.join(dest_root, question_folder_name)
            
        save_code_to_path(dest_folder, filename, ext, details['code'])
        print(f"  Saved to {dest_root}: {full_filename}")


def sync_to_local():
    # 1. Fetch your submissions list from the API
    submissions = get_all_accepted_submissions() 
    
    # 2. Process each one using our optimized function
    for sub in submissions:
        sync_submission(sub)


if __name__ == "__main__":
    sync_to_local()
