#!/usr/bin/python3
import time
import os
import concurrent.futures
import requests
from links import websites
import argparse

try:
    import fake_useragent
    fake_useragent_installed = True
except ImportError:
    fake_useragent_installed = False

parser = argparse.ArgumentParser(description="HideAndSeek Flags")
parser.add_argument('-v', '--verbose', dest="verbose", action='store_true', help='Verbose')
parser.add_argument('-o', '--output', dest="output_file", metavar="FILE", help='Output file path')
parser.add_argument('-s', '--silent', dest="silent", action='store_true', help='Silent mode')

args = parser.parse_args()
input_string = input("[+] Enter a username: ")
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
              ░                                  ░                                    \033[32m { Version 0.6 }\033[37m
                    Made with ❤️ by \033[33m SwiftGlitxh \033[37m\n
  [=]   \033[35m HideAndSeek is a small script to scan websites for a user \033[37m       [=]
  [=]   \033[36m             https://twitter.com/swiftglitxh                  \033[37m    [=]
  [=]   \033[35m   *** Please note not all sites will be 100% correct ***     \033[37m    [=]
''')
    print(f"  [\033[33m!\033[37m]\033[33m  Scanning '\033[32m{input_string}\033[33m' on {len(websites)} different platforms\033[37m\n")

def scan_website(website):
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

    if args.silent:
        return

    if args.output_file:
        with open(args.output_file, 'a') as file:
            file.write(output + '\n')
        print(output)
    else:
        print(output)

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
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(scan_website, websites)

if __name__ == "__main__":
    main()
