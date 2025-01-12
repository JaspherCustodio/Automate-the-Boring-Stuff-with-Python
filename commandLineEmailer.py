import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Ensure you have the necessary arguments
if len(sys.argv) != 3:
    print("Usage: python emailer.py <recipient_email> <message_text>")
    sys.exit(1)

# Get the command-line arguments
recipient_email = sys.argv[1]
message_text = sys.argv[2]

# Set up the Chrome WebDriver (make sure to specify your ChromeDriver path if necessary)
driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

# Open Gmail login page
driver.get("https://mail.google.com")

# Wait for the page to load
time.sleep(2)

# Login to Gmail (replace with your email and password, or use more secure methods like OAuth)
email_field = driver.find_element(By.ID, "identifierID")
email_field.send_keys("your_email@gmail.com")
email_field.send_keys(Keys.RETURN)

# Wait for the password page to load
time.sleep(2)

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("your_password") # Be cautious with hardcoding passwords
password_field.send_keys(Keys.RETURN)

# Wait for the inbox to load
time.sleep(5)

# Click the "Compos" button
compose_button = driver.find_element(By.CSS_SELECTOR, ".T-I.T-I-KE.L3")
compose_button.click()

# Wait for the compose window to open
time.sleep(2)

# Fill in the recipient email
to_field = driver.find_element(By.NAME, "to")
to_field .send_keys(reciient_email)

# Fill in the subject (optional)
subject_field = driver.find_element(By.NAME, "subjectbox")
subject_field.send_keys("Automated Email")

# Fill in the message body
body_field = driver.find_element(By.CSS_SELECTOR, ".Am.Al.editable.LW-avf.ts-tw")
body_field.send_keys(message_text)

# Send the email
send_button = driver.find_element(By.CSS_SELECTOR, ".T-I.J-J5-Ji.aoO.v7.T-I-ax7.L3")
send_button.click()

# Wait for the email to send
time.sleep(3)

# Close the browser
driver.quit()

print("Email sent successfully!")
