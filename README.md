# Easy Invite: WhatsApp Bulk Messaging

This project contains scripts for sending bulk messages (both text and images) via WhatsApp using Selenium. It can be used for sending invites, notifications, or any other messages to a list of contacts.

## Features

- **Bulk Text Messaging:** Send personalized text messages to a list of phone numbers.
- **Bulk Image Messaging:** Send an image to a list of phone numbers.

## Requirements

- Python 3.x
- Selenium
- pandas
- ChromeDriver

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/easy-invite.git
   cd easy-invite
   ```
2. **Install Required Packages:**
   Install the necessary Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. **Download ChromeDriver:**
  - Ensure you have the Chrome browser installed.
  - Download the appropriate ChromeDriver for your version of Chrome from [here](https://sites.google.com/chromium.org/driver/).
  - Place the ChromeDriver executable in the project directory and update the executable_path in the scripts accordingly.
4. **Prepare Your Guest List:**
  - Create a guests.csv file in the project directory with a column named Number containing the phone numbers of your contacts.
  - For bulk text messaging, add additional columns like Name for personalization.
5. **Set Up the WhatsApp Web Session:**
  - Run the script and scan the QR code with your WhatsApp mobile app.

## Usage
**Sending Text Messages**
  1. Open the whatsapp_text_sender.py script.
  2. Customize the message template as needed.
  3. Run the script:
  ```bash
  python3 whatsapp_text_sender.py
  ```

**Sending Image Messages**
  1. Open the whatsapp_image_sender.py script.
  2. Ensure the image path is correct.
  3. Run the script:
  ```bash
  python3 whatsapp_image_sender.py
  ```

## Important Notes
  - Make sure your phone has a stable internet connection during the process.
  - Test the script with a few numbers first before sending it to the entire list.
  - For the image script, you'll have to use the absolute image path.

## Disclaimer
  This project is for educational purposes only. Please use it responsibly and adhere to WhatsApp’s terms of service.
