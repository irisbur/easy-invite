import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load the guest list
df = pd.read_csv('guests.csv')

# Set up the Chrome driver
cService = ChromeService(executable_path='./chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=cService)
driver.get('https://web.whatsapp.com')
input('Scan the QR code and then press Enter to continue...')

# Path to the image
image_path = './invite.png'  # Ensure this is the correct path to your image

# Iterate over each guest in the list
for index, row in df.iterrows():
    number = row['Number']

    # Open chat with the number
    driver.get(f'https://web.whatsapp.com/send?phone={number}')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    time.sleep(5)  # Wait for the page to load

    # Click on the attach button (the plus icon)
    attach_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="plus"]'))
    )
    attach_button.click()

    # Click on the "Photos & Videos" button
    photos_videos_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Photos & videos")]'))
    )
    photos_videos_button.click()

    # Locate the file input for image attachments
    image_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'))
    )

    # Send the image path to the file input element
    image_input.send_keys(image_path)
    time.sleep(2)  # Wait for the image to upload

    # Send the image and emoji
    send_image_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))
    )
    send_image_button.click()
    time.sleep(5)  # Wait for the image and emoji to be sent

# Close the driver
driver.quit()
