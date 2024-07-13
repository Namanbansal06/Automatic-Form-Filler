from django.core.mail import EmailMessage
from django.conf import settings
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Function to capture screenshot using Selenium
def capture_screenshot(url):
    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(2)

    full_name_input = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    full_name_input.send_keys("Naman Bansal")

    phone_number = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    phone_number.send_keys("94579 xxxxx")

    email_address = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email_address.send_keys("fake@gmail.com")

    Home_Address = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    Home_Address.send_keys("XX-B Anonoymous colony")

    pin_number = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pin_number.send_keys("245 xxx")

    date_of_birth = driver.find_element(By.XPATH, '//input[@type="date"]')
    date_of_birth.send_keys("06/08/2xxx")
    date_of_birth.send_keys(Keys.RETURN)

    Gender = driver.find_element(By.XPATH,
                                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Gender.send_keys("Male")

    Verification = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Verification.send_keys("GNFPYC")

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(2)
    screenshot_path = 'form_submission_screenshot.png'
    driver.save_screenshot(screenshot_path)

    driver.quit()

    return screenshot_path


# Function to send email with screenshot attachment
def send_email_with_attachments(screenshot_path):
    subject = 'Python (Selenium) Assignment - Naman Bansal'
    message = ("Message"
               "\n\n\n For Source code:\n github repo : https://github.com/Namanbansal06/Automatic-Form-Filler")

    recipients = ['reciever@gmail.com']
    cc_recipients = ['reciever2@gmail.com']

    email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipients,
        cc=cc_recipients
    )

    resume_path = r"path"
    documentation_path = r"path"

    with open(screenshot_path, 'rb') as f:
        email.attach('screenshot.png', f.read(), 'image/png')

    # Attach the resume
    with open(resume_path, 'rb') as f:
        email.attach('resume.pdf', f.read(), 'application/pdf')

    # Attach Documentation file
    with open(documentation_path, 'rb') as f:
        email.attach('documentation.txt', f.read(), 'text/pdf/md')

        # Send email
    email.send()
    # return render(request, 'send_email/reh.html')


# Usage example
def send_screenshot_email(url):
    screenshot_path = capture_screenshot(url)


    send_email_with_attachments(screenshot_path)
    os.remove(screenshot_path)


url = "url"
send_screenshot_email(url)
