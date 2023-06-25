#!/bin/usr/python3
import time
import os
import concurrent.futures
import requests
from links import websites
import argparse

parser = argparse.ArgumentParser(description="HideAndSeek Flags")
parser.add_argument('-v', '--verbose', dest="verbose", action='store_true', help='Verbose')
parser.add_argument('-o', '--output', dest="output_file", metavar="FILE", help='Output file path')
parser.add_argument('-s', '--silent', dest="silent", action='store_true', help='Silent mode')

args = parser.parse_args()
input_string = input("[+] Enter a username: ")
try:
    os.system('cls')
except:
    os.system('clear')

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
              ░                                  ░                                    \033[32m { Version 0.8 }\033[37m
                    Made with ❤️ by \033[33m SwiftGlitxh \033[37m\n
  [=]   \033[35m HideAndSeek is a small script to scan websites for a user \033[37m       [=]
  [=]   \033[36m             https://twitter.com/swiftglitxh                  \033[37m    [=]
  [=]   \033[35m                                                              \033[37m    [=]
''')
    print(f"  [\033[33m!\033[37m]\033[33m  Scanning '\033[32m{input_string}\033[33m' on {len(websites)} different platforms\033[37m\n")

def scan_website(website):
    try:
        response = requests.get(website + input_string, timeout=3)
        if response.status_code == 200:
            if input_string in response.text:
                output = f"[\033[32m+\033[37m] [FOUND] \033[36m {website}{input_string}\033[33m  => \033[32m {input_string}\033[37m Found!"
            elif args.verbose:
                output = f"[\033[31m+\033[37m] [NO USER] \033[36m{website}{input_string}\033[33m  => \033[32m {input_string}\033[37m No User Found!"
            else:
                return
        else:
            return
    except requests.exceptions.RequestException:
        if args.verbose:
            output = f"[\033[31m+\033[37m] [DOWN] \033[36m {website}{input_string}\033[31m is down\033[37m"
        else:
            return

    if args.silent:
        return

    if args.output_file:
        with open(args.output_file, 'a') as file:
            file.write(output + '\n')
    else:
        print(output)

def main():
    banner()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(scan_website, websites)

    print('\n[\033[31m!\033[37m] SCAN COMPLETE!')

if __name__ == "__main__":
    main()
