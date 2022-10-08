#!/bin/usr/python3
import time
import os
import requests
import sys
from links import websites
import argparse

parser = argparse.ArgumentParser(description="HideAndSeek Flags")
parser.add_argument('-v',dest="verbose",action='store_true',help='Verbose')
parser.add_argument('--wildcard',dest="wildcard",action='store_true',help='Returns all as True')

args = parser.parse_args()
# Authory :: Swiftglitxh              
# Tool :: HideAndSeek                 
# Version :: 0.4                      
                    
try:
	os.system('cls')
except:
	os.system('clear')

def banner():
	print('''\033[31m
  ██░ ██  ██ ▓█████▄ ▓█████ ▄▄▄       ███▄    █ ▓█████▄   ██████ ▓█████ ▓█████  ██ ▄█▀
 ▓██░ ██▒▓██▒▒██▀ ██▌▓█   ▀▒████▄     ██ ▀█   █ ▒██▀ ██▌▒██    ▒ ▓█   ▀ ▓█   ▀  ██▄█▒ 
 ▒██▀▀██░▒██▒░██   █▌▒███  ▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌░ ▓██▄   ▒███   ▒███   ▓███▄░ 
 ░▓█ ░██ ░██░░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌  ▒   ██▒▒▓█  ▄ ▒▓█  ▄ ▓██ █▄ 
 ░▓█▒░██▓░██░░▒████▓ ░▒████▒▓█   ▓██▒▒██░   ▓██░░▒████▓ ▒██████▒▒░▒████▒░▒████▒▒██▒ █▄
  ▒ ░░▒░▒░▓   ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░░ ▒░ ░▒ ▒▒ ▓▒
  ▒ ░▒░ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ ░ ░▒  ░ ░ ░ ░  ░ ░ ░  ░░ ░▒ ▒░
  ░  ░░ ░ ▒ ░ ░ ░  ░    ░    ░   ▒      ░   ░ ░  ░ ░  ░ ░  ░  ░     ░      ░   ░ ░░ ░ 
  ░  ░  ░ ░     ░       ░  ░     ░  ░         ░    ░          ░     ░  ░   ░  ░░  ░   
              ░                                  ░                                    \033[32m { Version 0.6 }\033[37m
             		Made with ❤️ by \033[33m SwiftGlitxh \033[37m\n
  [=]   \033[35m HideAndSeek is a small script to scan websites for user \033[37m         [=]
  [=]   \033[36m             https://twitter.com/swiftglitxh                  \033[37m    [=]
  [=]   \033[35m                                                              \033[37m    [=]
''')
banner()
while True:
	username = input("[\033[31m=\033[37m] \033[33m Enter a username: \033[37m ").lower()
	if username == '':
		print('[=] Please enter a username.')
		print(username)
	else:
		break
time.sleep(0.1)
print(f"[\033[33m!\033[37m]\033[33m  Scanning '\033[32m{username}\033[33m' on {len(websites)} different platforms\033[37m\n")

# Check if website is up
start_time = time.time()
def scan(username):
	number=0
	ok = 0 
	not_found = 0 
	for x in websites:
		number +=1
		y = requests.head(x+username)
		url = x+username
		response = requests.post(url)

		if args.wildcard and args.verbose:
			print(f"[\033[32m+\033[37m] [FOUND] #{str(number)}\t\033[36m {x}{username}\033[33m\t{y.status_code}\033[37m" )

		elif args.wildcard:
			print(f"[\033[32m+\033[37m] [FOUND] #{str(number)}\t\033[36m {x}{username}\033[37m" )

		# VERBOSE ON 
		elif args.verbose:
			print(f"[\033[32m+\033[37m] [FOUND] #{str(number)}\t\033[36m {x}{username}\033[33m\t{y.status_code}\033[37m" )
			ok += 1

		else:

			if y.status_code == 200:	
				ok += 1 
				

				if username in str(response.content):	
					print(f"[\033[32m+\033[37m] [FOUND] #{str(number)}\t\033[36m {x}{username}\033[33m  => \033[32m {username}\033[37m Found!")

				else:
					pass
			if y.status_code == 404:
				not_found += 1 
				pass
			else:
				pass

	if args.verbose:
		print(f'''\n--------- SUMMARY ---------
	\n[\033[32m+\033[37m]Websites with '\033[32m200\033[37m' Response: \033[32m{ok}\033[37m\n[\033[31m+\033[37m]Websites with '\033[31m404\033[37m' Response: \033[31m{not_found}\033[37m''')
	# Scan time
		print(f'[\033[33m=\033[37m] Scanned \033[32m{len(websites)}\033[37m in {round(time.time() - start_time)} seconds ')
	else:
		pass
scan(username)
print('\n[\033[31m!\033[37m] SCAN COMPLETE!')