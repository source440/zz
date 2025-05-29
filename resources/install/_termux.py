from datetime import datetime
from os import path, system
from time import sleep

try:
    from colorama import Back, Fore, Style
except ModuleNotFoundError:
    print("Installing colorama...")
    system("pip install -q colorama")
    from colorama import Back, Fore, Style


def clear():
    system("clear")


MANDATORY_REQS = [
    "telethon",
    "gitpython",
    "telegraph",
    "requests",
    "pillow",
    "python-decouple",
    "youtube-search-python",
    "yt-dlp",
    "tabulate",
]
APT_PACKAGES = ["ffmpeg", "neofetch", "mediainfo"]
COPYRIGHT = f"Jmthon {datetime.now().year}"
HEADER = f"""
       __     ______  __  .__   __.  _______ .__   __.  _______ .__   __. 
\\ \\   / / __ \\|  | |  \\ |  | |   ____||  \\ |  | |   ____||  \\ |  | 
 \\ \\_/ / |  | |  | |   \\|  | |  |__   |   \\|  | |  |__   |   \\|  | 
  \\   /| |  | |  | |  . `  | |   __|  |  . `  | |   __|  |  . `  | 
   | | | |__| |  | |  |\\   | |  |____ |  |\\   | |  |____ |  |\\   | 
   |_|  \\____/|__| |__| \\__| |_______||__| \\__| |_______||__| \\__|"""

def with_header(text):
    return Fore.MAGENTA + HEADER + Fore.RESET + "\n\n" + text


def ask_process_apt_install():
    strm = input("").lower().strip()
    if strm == "e":
        print("Exiting...")
        exit(0)
    elif strm == "a":
        names = " ".join(APT_PACKAGES)
        print("Installing all apt-packages...")
        system(f"apt install {names} -y")
    elif strm != "s":
        print("Invalid input. Please try again.")
        ask_process_apt_install()


def create_gitignore_if_needed():
    if not path.exists(".gitignore"):
        with open(".gitignore", "w") as f:
            f.write(".env\n")
        print(f"{Fore.CYAN}* .gitignore file created and .env excluded.{Fore.RESET}")
    else:
        with open(".gitignore", "r+") as f:
            content = f.read()
            if ".env" not in content:
                f.write("\n.env\n")
                print(f"{Fore.CYAN}* .env added to existing .gitignore.{Fore.RESET}")
            else:
                print(f"{Fore.CYAN}* .env is already ignored in .gitignore.{Fore.RESET}")


def ask_make_env():
    print(f"{Fore.YELLOW}* Creating .env file with fixed API_ID and API_HASH...")
    with open(".env", "w") as file:
        file.write("API_ID=25978936\n")
        file.write("API_HASH=cf754dc655df0e7deff36732dbfff074\n")
        for var in ["SESSION", "BOT_TOKEN"]:
            inp = input(f"Enter {var}\n- ")
            file.write(f"{var}={inp}\n")
    print(f"{Fore.GREEN}* .env file created successfully!{Fore.RESET}")
    create_gitignore_if_needed()


# بداية السكربت
clear()
print(
    f"""
{Fore.GREEN}- Please review the terms and conditions for installation at the following link

يرجى قراءة شروط وأحكام التنصيب عبر الرابط التالي

https://t.me/YamenThon
. {Fore.RESET}
"""
)

print(with_header("Installing required packages..."))
system(f"pip install -q {' '.join(MANDATORY_REQS)}")

clear()
print(
    with_header(
        f"\n{Fore.GREEN}# Proceeding with APT package installation{Fore.RESET}\n\n"
    )
)
print("Choose an option:")
print(" - A = Install all APT packages")
print(" - S = Skip APT installation")
print(" - E = Exit\n")
ask_process_apt_install()

clear()

print(f"\n{Fore.RED}# Extra Features...\n")
inp = input(f"{Fore.YELLOW}* Do you want colored logs? [Y/N]: ").strip().lower()
if inp in ["yes", "y"]:
    print(f"{Fore.GREEN}Installing coloredlogs...")
    system("pip install -q coloredlogs")
else:
    print("Colored logs skipped.")

clear()

if not path.exists(".env"):
    print(with_header("Proceed to create .env file? [y/N] "))
    ask_make_env()

clear()
print(with_header(f"\n{Fore.GREEN}Installation complete! 🥳"))
sleep(0.2)
print(f"Use 'cd Source && python3 -m yamenthon' to run yamenthon.{Fore.RESET}")
sleep(0.5)
print("\nFor help, join @yamenthon.")
sleep(0.5)
print("\nMade by @yamenthon.")

system("pip uninstall -q colorama -y")
