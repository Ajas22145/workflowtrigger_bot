import os
from playwright.sync_api import sync_playwright

def start_seedloaf_server():
    email = os.getenv("SEEDLOAF_EMAIL")
    password = os.getenv("SEEDLOAF_PASSWORD")

    if not email or not password:
        raise ValueError("Seedloaf email or password environment variables are missing.")

    with sync_playwright() as p:
        # Launch headless browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Navigating to Seedloaf login page...")
        page.goto("https://seedloaf.com/login")
        
        # Fill in login credentials (adjust selectors if needed based on Seedloaf's form)
        page.fill("input[name='email']", email)
        page.fill("input[name='password']", password)
        page.click("button[type='submit']")
        
        print("Logged in successfully. Navigating to dashboard...")
        # Wait until redirected to dashboard
        page.wait_for_url("**/dashboard**", timeout=60000)
        
        print("Looking for the start server button...")
        # Click the start button on your server panel
        page.click("text=Start World") # Or change to a specific CSS selector like button.start-btn if needed
        
        print("Successfully triggered server start!")
        browser.close()

if __name__ == "__main__":
    start_seedloaf_server()
