import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

df = pd.read_csv('guests.csv')
cService = webdriver.ChromeService(executable_path='./chromedriver')
driver = webdriver.Chrome(service=cService)
driver.get('https://web.whatsapp.com')
input('Scan the QR code and then press Enter to continue...')

for index, row in df.iterrows():
    name = row['Name']
    number = row['Number']
    message = f"Hello {name}, please RSVP for our wedding here: https://forms.gle/W1FmrMiwiXJkg3ZQ8"

    # Open chat with the number
    driver.get(f'https://web.whatsapp.com/send?phone={number}&text={message}')
    time.sleep(10)  # Wait for the page to load

    # Send the message
    send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    send_button.click()
    time.sleep(5)  # Wait for the message to be sent

driver.quit()

