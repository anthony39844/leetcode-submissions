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
        # Use a longer timeout for the initial page load
        page.goto("https://leetcode.com/accounts/login/", wait_until="networkidle", timeout=60000)

        print("Filling credentials...")
        # Wait for the login input to be visible before interacting
        page.wait_for_selector('input[name="login"]', state="visible")
        page.fill('input[name="login"]', email)
        page.fill('input[name="password"]', password)

        print("Attempting to click Sign In...")
        # LeetCode sometimes uses an ID for the button; let's try the most common one
        submit_button = page.locator('button#signin_btn, button[type="submit"]')
        
        # Click and wait for the page to navigate away from the login screen
        # This is more reliable than waiting for a specific container
        try:
            with page.expect_navigation(timeout=30000):
                submit_button.click()
            print("Login successful - Page navigated.")
        except Exception as e:
            # If it fails, take a screenshot to help us debug (GitHub uploads this as an artifact if configured)
            page.screenshot(path="login_error.png")
            print(f"Login failed. It's possible a CAPTCHA appeared. Error: {e}")
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
