#!/usr/bin/python3
import time
import os
import concurrent.futures
import requests
from links import websites
import argparse
import pickle 

try:
    import fake_useragent
    fake_useragent_installed = True
except ImportError:
    fake_useragent_installed = False

parser = argparse.ArgumentParser(description="HideAndSeek Flags")
parser.add_argument('-v', '--verbose', dest="verbose", action='store_true', help='Verbose')
parser.add_argument('-s', '--store', dest="output_file", action='store_true', help='Output file path')

args = parser.parse_args()
os.system('clear')

def install_fake_useragent():
    os.system('pip install fake_useragent')

def banner():
    print('''\033[31m
  ██░ ██  ██ ▓█████▄ ▓█████ ▄▄▄       ███▄    █ ▓█████▄   ██████ ▓█████ ▓█████  ██ ▄█▀
 ▓██░ ██▒▓██▒▒██▀ ██▌▓█   ▀▒████▄     ██ ▀█   █ ▒██▀ ██▌▒██    ▒ ▓█   ▀ ▓█   ▀  ██▄█▒ 
 ▒██▀▀██░▒██▒░██   █▌▒███  ▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌░ ▓██▄   ▒███   ▒███   ▓███▄░ 
 ░▓█ ░██ ░██░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌  ▒   ██▒▒▓█  ▄ ▒▓█  ▄ ▓██ █▄ 
 ░▓█▒░██▓░██░░▒████▓ ░▒████▒▓█   ▓██▒▒██░   ▓██░░▒████▓ ▒██████▒▒░▒████▒░▒████▒▒██▒ █▄
  ▒ ░░▒░▒░▓   ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░░ ▒░ ░▒ ▒▒ ▓▒
  ▒ ░▒░ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ ░ ░▒  ░ ░ ░ ░  ░ ░ ░  ░░ ░▒ ▒░
  ░  ░░ ░ ▒ ░ ░ ░  ░    ░    ░   ▒      ░   ░ ░  ░ ░  ░ ░  ░  ░     ░      ░   ░ ░░ ░ 
  ░  ░  ░ ░     ░       ░  ░     ░  ░         ░    ░          ░     ░  ░   ░  ░░  ░   
              ░                                  ░                                    \033[32m { Version 0.7 }\033[37m
                    Made with ❤️ by \033[33m SwiftGlitxh \033[37m\n
  [=]   \033[35m HideAndSeek is a small script to scan websites for a user \033[37m       [=]
  [=]   \033[36m             https://twitter.com/swiftglitxh                  \033[37m    [=]
  [=]   \033[35m   *** Please note not all sites will be 100% correct ***     \033[37m    [=]
''')

def scan_website(website, input_string):
    try:
        user_agent = str(fake_useragent.UserAgent()) if fake_useragent_installed else None
        response = requests.get(website + input_string, timeout=3, headers={'User-Agent': user_agent})
        if response.status_code == 200:
            if input_string in response.text:
                output = f"[\033[32m+\033[37m] [FOUND] \033[36m {website}{input_string}\033[33m  => \033[32m {input_string}\033[37m Found!"
            elif args.verbose:
                output = f"[\033[31m+\033[37m] [NO USER] \033[36m{website}{input_string}\033[33m  => \033[32m {input_string}\033[37m No User Found!"
            else:
                return
        elif args.verbose:  # Added condition for verbose output when status code is not 200
            output = f"[\033[31m+\033[37m] [STATUS {response.status_code}] \033[36m{website}{input_string}\033[31m is down\033[37m"
        else:
            return
    except requests.exceptions.RequestException as e:
        if args.verbose:
            output = f"[\033[31m+\033[37m] [ERROR] \033[36m {website}{input_string}\033[31m encountered an error: {str(e)}\033[37m"
        else:
            return

    if args.output_file:
        store_output(website, input_string)
        print(output)
    else:
        print(output)


def store_output(website, input_string):
    if os.path.exists("database.pickle"):
        with open("database.pickle", "rb") as file:
            database = pickle.load(file)
    else:
        database = []

    database.append((website, input_string))

    with open("database.pickle", "wb") as file:
        pickle.dump(database, file)


def show_database():
    if os.path.exists("database.pickle"):
        with open("database.pickle", "rb") as file:
            database = pickle.load(file)

        print("Stored Database:")
        print("-" * 70)
        for entry in database:
            print(entry[0], entry[1])
        print("-" * 70)
    else:
        print("No database found.")

    input("\nPress any key to continue....")
    os.system("clear")
    banner()

def destroy_database():
    if os.path.exists("database.pickle"):
        os.remove("database.pickle")
        print("Database destroyed successfully.")
    else:
        print("No database found.")

    input("\nPress any key to continue....")
    os.system("clear")
    banner()


def main():
    if not fake_useragent_installed:
        print("[!] 'fake_useragent' library is not installed.")
        install = input("Do you want to install it? (y/n): ")
        if install.lower() == 'y':
            install_fake_useragent()
            print("\n[+] 'fake_useragent' library installed successfully.")
            time.sleep(1)
            os.system('clear')
            main()
        else:
            print("[!] 'fake_useragent' library is required for this script. Exiting...")
            return

    banner()

    while True:
        print("  [1] Scan Websites For Username")
        print("  [2] Show Collected Database")
        print("  [3] Destroy Database")
        print("  [0] Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            input_string = input("[+] Enter a username: ")
            print(f'\n\033[1;33m[+] Scanning for {input_string}...\033[0;37m')
            print('-'*70)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(scan_website, websites, [input_string] * len(websites))
            input("\nPress any key to continue....")
            os.system('clear')
            banner()    
        elif choice == "2":
            show_database()   
        elif choice == "3":
            destroy_database()     
        elif choice == "0":
            break
        else:
            print("\n[!] Invalid choice. Please try again.")
            input("\nPress any key to continue....")
            os.system('clear')
            banner()

if __name__ == "__main__":
    main()
