import os
import sys
from playwright.sync_api import sync_playwright

def main():
    email = os.getenv("LEETCODE_EMAIL")
    password = os.getenv("LEETCODE_PASSWORD")

    if not email or not password:
        print("Missing LeetCode credentials.")
        sys.exit(1)

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
        page = context.new_page()

        print("Navigating to LeetCode login...")
        page.goto("https://leetcode.com/accounts/login/")

        # Fill login form
        page.fill('input[name="login"]', email)
        page.fill('input[name="password"]', password)
        page.click('button[type="submit"]')

        # Wait for navigation to complete (logged in)
        try:
            page.wait_for_selector(".nav-item-container", timeout=15000)
            print("Login successful!")
        except:
            print("Login failed or timed out. Check credentials or CAPTCHA.")
            browser.close()
            sys.exit(1)

        # Extract cookies
        cookies = context.cookies()
        session_id = next((c['value'] for c in cookies if c['name'] == 'LEETCODE_SESSION'), None)
        csrf_token = next((c['value'] for c in cookies if c['name'] == 'csrftoken'), None)

        if session_id and csrf_token:
            # We print these in a special format that the Shell can capture
            print(f"RESULT_SESSION={session_id}")
            print(f"RESULT_CSRF={csrf_token}")
        else:
            print("Could not find cookies.")
            sys.exit(1)

        browser.close()

if __name__ == "__main__":
    main()
