from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Configuration
website_url = "https://example.com"  # Replace with the actual website URL
input_id = "email-1"  # ID of the email input field
submit_button_id = "submit-button"  # Replace with the actual ID of the submit button

# Read emails from a text file
with open("emails.txt", "r") as file:
    email_list = [line.strip() for line in file if line.strip()]

# Set up headless mode for Railway
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(website_url)

# Counters
a = 0  # Success count
b = 0  # Error count

# Loop through each email and submit it
for email in email_list:
    try:
        email_input = driver.find_element(By.ID, input_id)
        email_input.clear()
        email_input.send_keys(email)

        submit_button = driver.find_element(By.ID, submit_button_id)
        submit_button.click()

        a += 1  # Increment success counter

        # Print progress every 1000 emails
        if a % 1000 == 0:
            print(f"--> 1000 emails submitted <-- | Total now: {a}")

        time.sleep(2)  # Wait for form processing

    except Exception as e:
        print(f"Error submitting {email}: {e}")
        b += 1  # Increment error counter

# Close the browser
driver.quit()

# Summary
print("=======================================")
print(f"===> Total successful emails: {a} <===")
print(f"Total email submission errors: {b}")
