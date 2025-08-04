import smtplib
import getpass
import time
import re
import os
import random
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, Style, init

init(autoreset=True)

# ===== Tool login =====
tool_username = "admin"
tool_password = "admins"

# ===== Your personal Gmail credentials =====
your_email = "drwilliamsdrugsdealer@gmail.com"
your_app_password = "tulionnpiswncexy"

# ===== WhatsApp Business API credentials =====
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"
PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID_HERE"

# ===== WhatsApp support emails =====
support_emails = [
    "support@support.whatsapp.com",
    "web@support.whatsapp.com",
    "help@support.whatsapp.com",
    "appeals@support.whatsapp.com",
    "review@support.whatsapp.com"
] * 10

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def typewriter(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def check_whatsapp_number(phone):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/contacts"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "blocking": "wait",
        "contacts": [phone],
        "force_check": True
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        for contact in data.get("contacts", []):
            status = contact.get("status")
            wa_id = contact.get("wa_id", "N/A")
            print(Fore.GREEN + f"\n✅ Number: {wa_id} is {status.upper()} on WhatsApp.\n")
        if not data.get("contacts"):
            print(Fore.RED + "\n❌ Number is not registered on WhatsApp.\n")
    else:
        print(Fore.RED + "\n⚠️ Failed to check number.\n")
        print(response.text)

# ===== Login screen =====
while True:
    banner_color = random.choice([Fore.GREEN, Fore.CYAN, Fore.MAGENTA])
    print(banner_color + "📲 Welcome to WhatsApp Unban Tool")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    username = input("👤 Enter Username: ")
    password = getpass.getpass("🔒 Enter Password: ")

    if username == tool_username and password == tool_password:
        print(Fore.GREEN + "\n✅ Login successful!")

        # Banner art
        print(banner_color + '''
⠀⠀⠀    ⣠⣶⣶⣶⣶
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣧
⠀⠀⠀⠀⣼⣿⣿⣿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣠⣴⣶⣤⡀⠀
⠀⠀⠀⢰⣿⣿⣿⣿⠃⠈⢻⣿⣦⠀⠀⠀⠀⣸⣿⣿⣿⣿⣷⠀
⠀⠀⠀⠘⣿⣿⣿⡏⣴⣿⣷⣝⢿⣷⢀⠀⢀⣿⣿⣿⣿⡿⠋⠀
⠀⠀⠀⠀⢿⣿⣿⡇⢻⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣇⢸⣿⣿⡟⠙⠛⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀
⣴⣿⣿⣿⣿⣿⣿⣿⣠⣿⣿⡇⠀⠀⠀⠉⠛⣽⣿⣇⣀⣀⣀⠀
⠙⠻⠿⠿⠿⠿⠿⠟⠿⠿⠿⠇⠀⠀⠀⠀⠀⠻⠿⠿⠛⠛⠛
''')
        typewriter(Fore.YELLOW + "This tool was made by Crypto Lord alone.\n", delay=0.06)
        break
    else:
        print(Fore.RED + "\n❌ Incorrect credentials, try again...")
        time.sleep(2)

# ===== Main Menu =====
while True:
    clear()
    menu_color = random.choice([Fore.BLUE, Fore.YELLOW, Fore.CYAN])
    print(menu_color + "🛠️ WhatsApp Unban Tool - Main Menu")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(menu_color + " [1] 📩 Unban Temporary")
    print(menu_color + " [2] 🚫 Unban Permanent")
    print(menu_color + " [3] 🔍 Check WhatsApp Number Status")
    print(menu_color + " [0] ❌ Exit")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    choice = input(Fore.WHITE + "\n📥 Select an option: ").strip()

    if choice in ["1", "2"]:
        unban_type = "Temporary" if choice == "1" else "Permanent"
        clear()
        print(menu_color + f"🔄 Unban {unban_type} Selected\n")

        while True:
            phone = input("📞 Enter WhatsApp number with country code (e.g., +2348123456789): ").strip()
            if re.match(r"^\+\d{10,15}$", phone):
                break
            else:
                print(Fore.RED + "❌ Invalid format! Only numbers allowed with country code starting with +.")
                time.sleep(1)

        print(f"\n📝 Sending {unban_type} unban request for {phone}...")
        time.sleep(1)

        if unban_type == "Temporary":
            subject = "Request for Temporary Unban of WhatsApp Number"
            body = f"""
Dear WhatsApp Support Team,

I am writing to request a temporary unban for my WhatsApp number {phone}. I understand the importance of following WhatsApp's terms of service and apologize if my actions caused the temporary restriction.

Phone Number: {phone}
Device: Infinix Android 10
WhatsApp Version: 2.24.x.x

I kindly ask that you review my case and reinstate my account. Thank you for your time and assistance.

Best regards,
User
"""
        else:
            subject = "Urgent Request for Permanent Unban of WhatsApp Number"
            body = f"""
Dear WhatsApp Appeals Team,

I am writing to appeal the permanent ban placed on my WhatsApp number {phone}. I believe this may have been a mistake or misunderstanding, and I am kindly asking for a thorough review of my account status.

Phone Number: {phone}
Device: Infinix Android 10
WhatsApp Version: 2.24.x.x

Please consider lifting this ban, and allow me to continue using your service. I value the platform greatly and will adhere to all community guidelines moving forward.

Sincerely,
User
"""

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(your_email, your_app_password)

            for i, email in enumerate(support_emails, 1):
                msg = MIMEMultipart()
                msg['From'] = your_email
                msg['To'] = email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                server.send_message(msg)
                print(Fore.GREEN + f"   [{i}/50] Sent to {email}")
                time.sleep(0.2)

            server.quit()
            print(Fore.GREEN + f"\n🎉 SUCCESS: {unban_type} unban request submitted.")
            print("📡 Stay active while WhatsApp reviews your request.\n")

        except Exception as e:
            print(Fore.RED + "\n❌ Failed to send email:", e)
        input(Fore.CYAN + "\n🔁 Press Enter to return to menu...")

    elif choice == "3":
        clear()
        print(menu_color + "🔍 Check WhatsApp Number Status\n")
        phone = input("📞 Enter the WhatsApp number (e.g., +2348123456789): ")
        print("\n⏳ Checking number...")
        time.sleep(1.5)
        check_whatsapp_number(phone)
        input(Fore.CYAN + "\n🔁 Press Enter to return to menu...")

    elif choice == "0":
        print(Fore.YELLOW + "\n👋 Goodbye!")
        break

    else:
        print(Fore.RED + "\n❌ Invalid choice.")
        time.sleep(2)