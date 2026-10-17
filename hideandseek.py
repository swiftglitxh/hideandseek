#!/usr/bin/python3
import os
import time
import argparse
import concurrent.futures

import requests
import praw
from links import websites
from bs4 import BeautifulSoup

try:
    import fake_useragent
    fake_useragent_installed = True
except ImportError:
    fake_useragent_installed = False

parser = argparse.ArgumentParser(description="HideAndSeek Flags")
parser.add_argument('-v', '--verbose', dest="verbose", action='store_true', help='Verbose')
parser.add_argument('-D', '--deep', dest="deep", action='store_true', help='D33P SC4N')
args = parser.parse_args()

# ─── Credentials (set these as environment variables, never hardcode them) ──
REDDIT_CLIENT_ID = os.environ.get("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.environ.get("REDDIT_CLIENT_SECRET")
TWITCH_CLIENT_ID = os.environ.get("TWITCH_CLIENT_ID")
TWITCH_ACCESS_TOKEN = os.environ.get("TWITCH_ACCESS_TOKEN")

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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
                ░                                  ░                                    \033[1;32m { Version 0.9 }\033[0;37m
                    Made with ❤️ by \033[33m SwiftGlitxh \033[37m\n
  [=]  \033[35m HideAndSeek is a small script to scan websites for a user\033[37m  [=]
  [=]   \033[36m             https://twitter.com/swiftglitxh                  \033[37m      [=]
  [=]   \033[32m   *** Please note not all sites will be 100% correct ***     \033[37m      [=]
''')
    if args.deep:
        print("\033[1;33;4mDeep scan enabled\033[0;37;0m = \033[0;32mTrue\033[0;37m")
    else:
        print("\033[1;33;4mDeep scan enabled\033[0;37;0m = \033[0;31mDisabled\033[0;37m")
    print("")


def scan_website(website, input_string):
    try:
        user_agent = str(fake_useragent.UserAgent()) if fake_useragent_installed else DEFAULT_USER_AGENT
        target_url = website + input_string
        response = requests.get(target_url, timeout=5, headers={'User-Agent': user_agent})

        if response.status_code == 200 and input_string in response.text:
            output = f"[\033[32m+\033[37m] [FOUND] \033[36m{target_url}\033[33m  => \033[32m{input_string}\033[37m Found!"
            print(output)

            if args.deep:
                if "reddit.com/user" in target_url:
                    Social.reddit(input_string)
                elif "twitch.tv" in target_url:
                    Social.twitch(input_string)
                elif "github.com" in target_url:
                    Social.github(input_string)
                elif "steamcommunity.com" in target_url:
                    Social.Steam(input_string)
                elif "pinterest.com" in target_url:
                    Social.Pinterest(input_string)
                elif "ask.fm" in target_url:
                    Social.AskFM(input_string)
                elif "codecademy.com" in target_url:
                    Social.Codecademy(input_string)

        elif args.verbose:
            if response.status_code == 200:
                print(f"[\033[31m+\033[37m] [NO USER] \033[36m{target_url}\033[33m  => \033[32m{input_string}\033[37m No User Found!")
            else:
                print(f"[\033[31m+\033[37m] [STATUS {response.status_code}] \033[36m{target_url}\033[31m Not Found\033[37m")

    except requests.exceptions.RequestException as e:
        if args.verbose:
            print(f"[\033[31m+\033[37m] [ERROR] \033[36m{website}{input_string}\033[31m encountered an error: {e}\033[37m")


class Social:

    @staticmethod
    def reddit(input_string):
        if not REDDIT_CLIENT_ID or not REDDIT_CLIENT_SECRET:
            print("[!] Reddit credentials not configured. Set REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET.")
            return

        try:
            reddit = praw.Reddit(
                client_id=REDDIT_CLIENT_ID,
                client_secret=REDDIT_CLIENT_SECRET,
                user_agent="HideAndSeek/0.9"
            )
            user = reddit.redditor(input_string)

            print(f'''\033[1;31m\nR |\t\033[1;31;4mREDDIT INFORMATION GATHERED\033[0;37;0m\n\033[1;31mE |\033[0;37m
\033[1;31mD |\033[0;37m\033[32m   - \033[37mUsername: {user.name} (u/{user.name})
\033[1;31mD |\033[0;37m\033[32m   - \033[37mKarma: {user.link_karma}
\033[1;31mI |\033[0;37m\033[32m   - \033[37mCake day: {user.created_utc}\n''')
        except Exception as e:
            print(f"[!] Reddit lookup failed: {e}")

    @staticmethod
    def Pinterest(input_string):
        try:
            url = f'https://in.pinterest.com/{input_string.capitalize()}/'
            response = requests.get(url, headers={'User-Agent': DEFAULT_USER_AGENT}, timeout=5)
            soup = BeautifulSoup(response.content, "html.parser")

            name = soup.find('div', class_='FNs zI7 iyn Hsu')
            username = soup.find('div', class_='jzS un8 C9i U1N')
            followers = soup.find('div', class_='tBJ dyH iFc sAJ O2T zDA IZT H2s')
            following = soup.find('div', class_='Jea hs0 zI7 iyn Hsu')

            print(f"\n\033[1;31mP |\t\033[1;31;4mPINTEREST INFORMATION GATHERED\033[0;37;0m")
            print(f"\033[1;31mI |\033[0;37m\033[32m   - \033[37mName:", name.text if name else "N/A")
            print(f"\033[1;31mN |\033[0;37m\033[32m   - \033[37mUsername:", username.text if username else "N/A")
            print(f"\033[1;31mT |\033[0;37m\033[32m   - \033[37mFollowing:", following.text if following else "N/A")
            print(f"\033[1;31mE |\033[0;37m\033[32m   - \033[37mFollowers:", followers.text if followers else "N/A")
            print(f"\033[1;31mR |\033[0;37m\033[32m   - \033[37mUser Profile:", url)
            print("\033[1;31mE |\n\033[1;31mS |\n\033[1;31mT |\n\033[1;37m")
        except requests.exceptions.RequestException as e:
            print(f"[!] Pinterest lookup failed: {e}")

    @staticmethod
    def AskFM(input_string):
        try:
            url = f'https://ask.fm/{input_string}'
            response = requests.get(url, headers={'User-Agent': DEFAULT_USER_AGENT}, timeout=5)
            soup = BeautifulSoup(response.content, "html.parser")

            name = soup.find('span', class_='ellipsis lh-spacy')
            username = soup.find('span', class_='d-flex flex-items-center gap-2 text-white text-small text-shadow')
            profile_posts = soup.find('div', class_='profileTabAnswerCount text-large')
            profile_likes = soup.find('div', class_='profileTabLikeCount text-large')

            print(f"\033[1;31m\nA |\t\033[1;31;4mASKFM INFORMATION GATHERED\033[0;37;0m")
            print('\033[1;31mS |\033[0;37m\033[32m   -\033[0;37m Name:', name.text if name else "N/A")
            print('\033[1;31mK |\033[0;37m\033[32m   -\033[0;37m Username:', username.text if username else "N/A")
            print('\033[1;31m• |\033[0;37m\033[32m   -\033[0;37m Posts:', profile_posts.text if profile_posts else "N/A")
            print('\033[1;31mF |\033[0;37m\033[32m   -\033[0;37m Likes:', profile_likes.text if profile_likes else "N/A")
            print('\033[1;31mM |\033[0;37m\033[32m   -\033[0;37m Link:', url)
            print("")
        except requests.exceptions.RequestException as e:
            print(f"[!] AskFM lookup failed: {e}")

    @staticmethod
    def Steam(input_string):
        try:
            url = f"https://steamid.xyz/{input_string}"
            response = requests.get(url, headers={'User-Agent': DEFAULT_USER_AGENT}, timeout=5)
            soup = BeautifulSoup(response.content, "html.parser")
            inputs = soup.find_all('input')

            if len(inputs) >= 9:
                nickname = inputs[6].get('value', "N/A")
                profile_value = inputs[8].get('value', "N/A")
                profile_link = inputs[5].get('value', "N/A")

                print(f'''\n\033[1;33mS  |\t\033[1;33;4mSTEAM INFORMATION GATHERED\033[0;37;0m
\033[1;33mT  |\033[0;37m    -  {input_string} ID: {profile_link}
\033[1;33mE  |\033[0;37m    -  {input_string} Nickname: {nickname}
\033[1;33mA  |\033[0;37m    -  {input_string} Link:  {profile_value}
\033[1;33mM  |\033[1;37m\n''')
            else:
                print(f"[!] Steam profile data not found for {input_string}")
        except requests.exceptions.RequestException as e:
            print(f"[!] Steam lookup failed: {e}")

    @staticmethod
    def Codecademy(input_string):
        try:
            url = f"https://www.codecademy.com/profiles/{input_string}"
            response = requests.get(url, headers={'User-Agent': DEFAULT_USER_AGENT}, timeout=5)
            soup = BeautifulSoup(response.content, 'html.parser')

            username = soup.find('span', class_='gamut-1bq9uel-Text e1xvzpfm2')
            infos = soup.find(class_='gamut-10adrv7-Text e1xvzpfm0')
            titles = soup.find_all(class_='gamut-hmhp7h-Text e8i0p5k0')
            course_info = soup.find('h3', class_='gamut-1jmkub7-Text e8i0p5k0')
            badge_info = soup.find_all(class_='gamut-sxeb1z-Text e8i0p5k0')
            badge_link = soup.find('a', class_='e1w6mdco0 gamut-syg06f-ResetElement-createButtonComponent e1bhhzie0')
            profile_image = soup.find('img', class_='gamut-1qfpxq1 etnxc150')

            print(f'''\n\033[1;33mC  |\t\033[1;33;4mCODECADEMY INFORMATION GATHERED\033[0;37;0m
\033[1;33mO  |\033[0;37m    -  Username: {username.text if username else "N/A"}
\033[1;33mD  |\033[0;37m    -  Active: {infos.text if infos else "N/A"}
\033[1;33mE  |\033[0;37m    -  {titles[1].text if len(titles) > 1 else "N/A"}:
\033[1;33mC  |\033[0;37m    >  \033[34m{course_info.text if course_info else "N/A"}\033[37m
\033[1;33mA  |\033[0;37m    >  {titles[2].text if len(titles) > 2 else "N/A"}
\033[1;33mD  |\033[0;37m    -  \033[34m{badge_info[0].text if len(badge_info) > 0 else "N/A"}\033[37m
\033[1;33mE  |\033[0;37m    -  \033[34m{badge_info[1].text if len(badge_info) > 1 else "N/A"}\033[37m
\033[1;33mM  |\033[0;37m    >  Badge Link: {"https://www.codecademy.com" + badge_link.get('href') if badge_link else "N/A"}
\033[1;33mY  |\033[0;37m    -  Profile Image: {profile_image['src'] if profile_image else "N/A"}\n''')
        except requests.exceptions.RequestException as e:
            print(f"[!] Codecademy lookup failed: {e}")

    @staticmethod
    def twitch(input_string):
        if not TWITCH_CLIENT_ID or not TWITCH_ACCESS_TOKEN:
            print("[!] Twitch credentials not configured. Set TWITCH_CLIENT_ID / TWITCH_ACCESS_TOKEN.")
            return

        headers = {
            'Client-ID': TWITCH_CLIENT_ID,
            'Authorization': f'Bearer {TWITCH_ACCESS_TOKEN}'
        }

        try:
            user_resp = requests.get(
                f'https://api.twitch.tv/helix/users?login={input_string}',
                headers=headers, timeout=5
            )
            user_data = user_resp.json()
            if not user_data.get('data'):
                print(f"[!] No Twitch user found for {input_string}")
                return
            login_id = user_data['data'][0]['id']

            schedule_resp = requests.get(
                f'https://api.twitch.tv/helix/schedule?broadcaster_id={login_id}',
                headers=headers, timeout=5
            )
            schedule_data = schedule_resp.json()
            try:
                name = schedule_data['data']['segments'][0]['category']['name']
                clock = schedule_data['data']['segments'][0]['start_time']
            except (KeyError, IndexError, TypeError):
                name = "No Schedule Found"
                clock = "No Time Found"

            followers_resp = requests.get(
                f'https://api.twitch.tv/helix/channels/followers?broadcaster_id={login_id}',
                headers=headers, timeout=5
            )
            followers = "N/A"
            if followers_resp.status_code == 200:
                followers = followers_resp.json().get('total', "N/A")
            else:
                print(f"[!] Failed to retrieve follower list. Status code: {followers_resp.status_code}")

            print("\n\033[35mT |\033[0;37m\t\033[1;35;4mTWITCH INFORMATION GATHERED\033[0;37;0m")
            print(f'''\033[35mW |\033[0;37m\033[32m   - \033[37mUsername: {input_string}
\033[35mI |\033[0;37m\033[32m   - \033[37mFollowers: {followers}
\033[35mT |\033[0;37m\033[32m   - \033[37mSchedule: {name}
\033[35mC |\033[0;37m\033[32m   - \033[37mSchedule Time: {clock}
\033[35mH |\033[0;37m\n''')
        except requests.exceptions.RequestException as e:
            print(f"[!] Twitch lookup failed: {e}")

    @staticmethod
    def github(input_string):
        try:
            response = requests.get(f"https://github.com/{input_string}", timeout=5)
            if response.status_code != 200:
                print(f"[-] GitHub profile not found for {input_string}")
                return

            print("\n\033[32mG |\033[0;37m\t\033[1;32;4mGITHUB INFORMATION GATHERED\033[0;37;0m")
            soup = BeautifulSoup(response.text, "html.parser")

            name_element = soup.find("span", class_="p-name")
            if name_element:
                print(f"\033[32mI |\033[0;37m\033[32m    - \033[37mUsername: {name_element.text.strip()}")

            location_element = soup.find("li", itemprop="homeLocation")
            if location_element:
                print(f"\033[32mT |\033[0;37m\033[32m    - \033[37mLocation: {location_element.text.strip()}")
            else:
                print(f"\033[32mT |\033[0;37m\033[32m    - \033[37mLocation:\033[31m No Location Found\033[37m")

            website_element = soup.find("li", itemprop="url")
            if website_element and website_element.a:
                print(f"\033[32mH |\033[0;37m\033[32m    - \033[37mWebsite: {website_element.a['href']}")
            else:
                print(f"\033[32mH |\033[0;37m\033[32m    - \033[37mWebsite:\033[31m No Website Found\033[37m")

            followers_element = soup.find("a", href=f"https://github.com/{input_string}?tab=followers")
            if followers_element and followers_element.span:
                print(f"\033[32mU |\033[0;37m\033[32m    - \033[37mFollowers: {followers_element.span.text.strip()}")

            following_element = soup.find("a", href=f"https://github.com/{input_string}?tab=following")
            if following_element and following_element.span:
                print(f"\033[32mB |\033[0;37m\033[32m    - \033[37mFollowing: {following_element.span.text.strip()}")

            contributions_element = soup.find("span", class_="ContributionCalendar-day")
            if contributions_element and contributions_element.has_attr("data-count"):
                print(f"\033[32mU |\033[0;37m\033[32m    - \033[37mContributions: {contributions_element['data-count']}")

            print("\n")

        except requests.exceptions.RequestException as e:
            print(f"[!] GitHub lookup failed: {e}")


def main():
    if not fake_useragent_installed:
        print("[!] 'fake_useragent' library is not installed.")
        install = input("Do you want to install it? (y/n): ")
        if install.lower() == 'y':
            install_fake_useragent()
            print("\n[+] 'fake_useragent' library installed successfully.")
            time.sleep(1)
            clear_screen()
            main()
            return
        else:
            print("[!] 'fake_useragent' library is required for this script. Exiting...")
            return

    clear_screen()
    banner()

    while True:
        print("  [1] Scan Websites For Username")
        print("  [0] Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            input_string = input("[+] Enter a username: ").strip()
            if not input_string:
                print("[!] Username cannot be empty.")
                input("\nPress any key to continue....")
                clear_screen()
                banner()
                continue

            print(f'\n[+] Scanning for {input_string}...')
            print('-' * 70)
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                for website in websites:
                    executor.submit(scan_website, website['url'], input_string)

            input("\nPress any key to continue....")
            clear_screen()
            banner()

        elif choice == "0":
            break
        else:
            print("\n[!] Invalid choice. Please try again.")
            input("\nPress any key to continue....")
            clear_screen()
            banner()


if __name__ == "__main__":
    main()
