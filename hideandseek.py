#!/usr/bin/python3
import time,os,requests,argparse,praw
import concurrent.futures
from links import websites
from bs4 import BeautifulSoup
from googlesearch import search
try:
    import fake_useragent
    fake_useragent_installed = True
except ImportError:
    fake_useragent_installed = False

parser = argparse.ArgumentParser(description="HideAndSeek Flags")
parser.add_argument('-v', '--verbose', dest="verbose", action='store_true', help='Verbose')
parser.add_argument('-D', '--deep', dest="deep", action='store_true', help='D33P SC4N')
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
                ░                                  ░                                    \033[1;32m { Version 0.8 }\033[0;37m
                    Made with ❤️ by \033[33m SwiftGlitxh \033[37m\n
  [=]  \033[35m HideAndSeek is a small script to scan websites for a user and more\033[37m  [=]
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
        user_agent = str(fake_useragent.UserAgent()) if fake_useragent_installed else None
        response = requests.get(website + input_string, timeout=3, headers={'User-Agent': user_agent})

        if response.status_code == 200:
            if input_string in response.text:
                time.sleep(2)
                output = f"[\033[32m+\033[37m] [FOUND] \033[36m {website}{input_string}\033[33m  => \033[32m {input_string}\033[37m Found!"
                print(output)
            if f"https://reddit.com/user/{input_string}" in output:
                if args.deep:
                    Social.reddit(input_string)
                
            if f"https://www.twitch.tv/{input_string}" in output:
                if args.deep:
                    Social.twitch(input_string)

            if f'https://github.com/{input_string}' in output:
                if args.deep:
                    Social.github(input_string)

            if f'https://steamcommunity.com/id/{input_string}' in output: 
                if args.deep:
                    Social.Steam(input_string)

            if f'https://in.pinterest.com/{input_string}' in output:
                if args.deep:
                    Social.Pinterest(input_string)

            if f'https://ask.fm/{input_string}' in output:
                print(output)
                if args.deep:
                    Social.AskFM(input_string)
            if f"https://www.codecademy.com/profiles/{input_string}" in output:
                if args.deep:
                    Social.Codecademy(input_string)
            elif args.verbose:  # Assuming args.verbose is a global variable
                output = f"[\033[31m+\033[37m] [NO USER] \033[36m{website}{input_string}\033[33m  => \033[32m {input_string}\033[37m No User Found!"
        elif args.verbose:  # Assuming args.verbose is a global variable
            output = f"[\033[31m+\033[37m] [STATUS {response.status_code}] \033[36m{website}{input_string}\033[31m 404 Page Not Found\033[37m"
    except requests.exceptions.RequestException as e:
        if args.verbose:  # Assuming args.verbose is a global variable
            output = f"[\033[31m+\033[37m] [ERROR] \033[36m {website}{input_string}\033[31m encountered an error: {str(e)}\033[37m"
        else:
            return

class Social:        
    def reddit(input_string):
        # Initialize the Reddit API client
        reddit = praw.Reddit(
            client_id='H6RsGi_YBuecXkOV7V0nwg',
            client_secret='-gHM_eRNYyO5UyHc5vYhHCFvbiMdzA',
            user_agent=f'HideAndSeek/0.7'
        )

        username = input_string
        user = reddit.redditor(username)

        # Display Reddit profile information
        print(f'''\033[1;31m\nR |\t\033[1;31;4mREDDIT INFORMATION GATHERED\033[0;37;0m\n\033[1;31mE |\033[0;37m
\033[1;31mD |\033[0;37m\033[32m   - \033[37mUsername: {user.name} (u/{user.name})
\033[1;31mD |\033[0;37m\033[32m   - \033[37mKarma: {user.link_karma}
\033[1;31mI |\033[0;37m\033[32m   - \033[37mCake day: {user.created_utc}
\033[1;31mT |\033[0;37m\033[32m   - \033[37mProfile: {output}\n''')
    
    def Pinterest(input_string):
        url = f'https://in.pinterest.com/{input_string.capitalize()}/'
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        response = requests.get(url,headers={'User-Agent': user_agent})
        soup = BeautifulSoup(response.content, "html.parser")
        name = soup.find('div',class_='FNs zI7 iyn Hsu')
        username = soup.find('div',class_='jzS un8 C9i U1N')
        followers = soup.find('div',class_='tBJ dyH iFc sAJ O2T zDA IZT H2s')
        following = soup.find('div',class_='Jea hs0 zI7 iyn Hsu')

        print(f"\n\033[1;31mP |\t\033[1;31;4mPENTERESTINFORMATION GATHERED\033[0;37;0m")
        print(f"\033[1;31mI |\033[0;37m\033[32m   - \033[37mName:",name.text)
        print(f"\033[1;31mN |\033[0;37m\033[32m   - \033[37mUsername:",username.text)
        print(f"\033[1;31mT |\033[0;37m\033[32m   - \033[37mfollowing:",following.text)
        print(f"\033[1;31mE |\033[0;37m\033[32m   - \033[37mFollowers:",followers.text)
        print(f"\033[1;31mR |\033[0;37m\033[32m   - \033[37mUser Profile:",url)
        print("\033[1;31mE |\n\033[1;31mS |\n\033[1;31mT |\n\033[1;37m")

    def AskFM(input_string):
        url = f'https://ask.fm/{input_string}'
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        response = requests.get(url,headers={'User-Agent': user_agent})
        soup = BeautifulSoup(response.content, "html.parser")

        name = soup.find('span',class_='ellipsis lh-spacy')
        username = soup.find('span',class_='d-flex flex-items-center gap-2 text-white text-small text-shadow')
        profile_posts = soup.find('div',class_='profileTabAnswerCount text-large')
        profile_likes = soup.find('div',class_='profileTabLikeCount text-large')

        print(f"\033[1;31m\nA |\t\033[1;31;4mASKFM INFORMATION GATHERED\033[0;37;0m")
        print('\033[1;31mS |\033[0;37m\033[32m   -\033[0;37m Name:',name.text)
        print('\033[1;31mK |\033[0;37m\033[32m   -\033[0;37m Username:',username.text)
        print('\033[1;31m• |\033[0;37m\033[32m   -\033[0;37m Posts:',profile_posts.text)
        print('\033[1;31mF |\033[0;37m\033[32m   -\033[0;37m Likes:',profile_likes.text)
        print('\033[1;31mM |\033[0;37m\033[32m   -\033[0;37m Link:',url)
        print("")

    def Steam(input_string):
       
        url = f"https://steamid.xyz/{input_string}"
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        response = requests.get(url,headers={'User-Agent': user_agent})
        soup = BeautifulSoup(response.content, "html.parser")
        link = soup.find_all('input')
        # Check if the fourth input tag exists
        if len(link) >= 5:
            nickname = link[6]  # Fourth input tag (zero-based index)
            fourth_input = link[8]  # Fourth input tag (zero-based index)
            profile_link = link[5]  # Fourth input tag (zero-based index)
            link = profile_link.get('value')
            value = fourth_input.get('value')
            nick = nickname.get('value')

            print(f'''\n\033[1;33mS  |\t\033[1;33;4mSTEAM INFORMATION GATHERED\033[0;37;0m
\033[1;33mT  |\033[0;37m    -  {input_string} ID: {link}
\033[1;33mE  |\033[0;37m    -  {input_string} Nickname: {nick}
\033[1;33mA  |\033[0;37m    -  {input_string} Link:  {value}
\033[1;33mM  |\033[1;37m\n''')


    def Codecademy(input_string):
        url = f"https://www.codecademy.com/profiles/{input_string}"
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        response = requests.get(url, headers={'User-Agent': user_agent})
        soup = BeautifulSoup(response.content, 'html.parser')
        profile_image = soup.find('img', class_='gamut-1qfpxq1 etnxc150')
        username = soup.find('span', class_='gamut-1bq9uel-Text e1xvzpfm2')
        infos = soup.find(class_='gamut-10adrv7-Text e1xvzpfm0')
        titles = soup.find_all(class_='gamut-hmhp7h-Text e8i0p5k0')
        course_info = soup.find('h3', class_='gamut-1jmkub7-Text e8i0p5k0')
        badge_info = soup.find_all(class_='gamut-sxeb1z-Text e8i0p5k0')
        badge_link = soup.find('a', class_='e1w6mdco0 gamut-syg06f-ResetElement-createButtonComponent e1bhhzie0')

        print(f'''\n\033[1;33mC  |\t\033[1;33;4mCODECADEMY INFORMATION GATHERED\033[0;37;0m
\033[1;33mO  |\033[0;37m    -  Username: {username.text}
\033[1;33mD  |\033[0;37m    -  Active: {infos.text}
\033[1;33mE  |\033[0;37m    -  {titles[1].text}:
\033[1;33mC  |\033[0;37m    >  \033[34m{course_info.text}\033[37m
\033[1;33mA  |\033[0;37m    >  {titles[2].text}
\033[1;33mD  |\033[0;37m    -  \033[34m{badge_info[0].text}\033[37m
\033[1;33mE  |\033[0;37m    -  \033[34m{badge_info[1].text}\033[37m
\033[1;33mM  |\033[0;37m    >  Badge Link: https://www.codecademy.com{badge_link.get('href')}
\033[1;33mY  |\033[0;37m    -  Profile Image: {profile_image['src']}\n''')

  
    def twitch(input_string):
        username = 'swiftglitxh'
        client_id = 'ih8uqatoautizc0g8nwiaceikimdxn'
        access_token = '0wxifp5qbt0sq4lat1qdywox41p4hh'
        # Set the headers with the required authentication
        headers = {
            'Client-ID': client_id,
            'Authorization': f'Bearer {access_token}'
        }
        user_id = requests.get(f'https://api.twitch.tv/helix/users?login={input_string}',headers=headers)
        name = user_id.json()
        login = name['data'][0]['id']
        login_id = login
        # Set up the API endpoint URL
        url = f'https://api.twitch.tv/helix/channels/followers?broadcaster_id={login_id}'
        sheschedule = f'https://api.twitch.tv/helix/schedule?broadcaster_id={login_id}'

        time = requests.get(sheschedule, headers=headers)
        d = time.json()
        try:
            name = d['data']['segments'][0]['category']['name']
            clock = d['data']['segments'][0]['start_time']
        except:
            name = "No Schedule Found"
            clock = "No Time Found"
        response = requests.get(url, headers=headers)

        # Check the response status code
        if response.status_code == 200:
            data = response.json()
            followers = data.get('total')
        else:
            print(f'Failed to retrieve follower list. Status code: {response.status_code}')
        
        # Display Twitch profile information
        print("\n\033[35mT |\033[0;37m\t\033[1;35;4mTWITCH INFORMATION GATHERED\033[0;37;0m")
        print(f'''\033[35mW |\033[0;37m\033[32m   - \033[37mUsername: {input_string}
\033[35mI |\033[0;37m\033[32m   - \033[37mFollowers: {followers}
\033[35mT |\033[0;37m\033[32m   - \033[37mSheschedule: {name}
\033[35mC |\033[0;37m\033[32m   - \033[37mSheschedule Time: {clock}
\033[35mH |\033[0;37m\n''') 
            
    def github(input_string):
        try:
            response = requests.get(f"https://github.com/{input_string}")
            if response.status_code == 200:
                print("\n\033[32mG |\033[0;37m\t\033[1;32;4mGITHUB INFORMATION GATHERED\033[0;37;0m")
                soup = BeautifulSoup(response.text, "html.parser")
                name_element = soup.find("span", class_="p-name")

                if name_element:
                    print(f"\033[32mI |\033[0;37m\033[32m    - \033[37mUsername:{name_element.text.strip()}")

                location_element = soup.find("li", itemprop="homeLocation")
                if location_element:
                    print(f"\033[32mT |\033[0;37m\033[32m    - \033[37mLocation: {location_element.text.strip()}")
                else:
                    print(f"\033[32mT |\033[0;37m\033[32m    - \033[37mLocation:\033[31m No Location Found\033[37m")
                website_element = soup.find("li", itemprop="url")

                if website_element:
                    print(f"\033[32mH |\033[0;37m\033[32m    - \033[37mWebsite: {website_element.a['href']}")
                else:
                    print(f"\033[32mH |\033[0;37m\033[32m    - \033[37mWebsite:\033[31m No Website Found\033[37m")
                followers_element = soup.find("a", href=f"https://github.com/{input_string}?tab=followers")
                
                if followers_element:
                    print(f"\033[32mU |\033[0;37m\033[32m    - \033[37mFollowers: {followers_element.span.text.strip()}")
                following_element = soup.find("a", href=f"https://github.com/{input_string}?tab=following")

                if following_element:
                    print(f"\033[32mB |\033[0;37m\033[32m    - \033[37mFollowing: {following_element.span.text.strip()}")
                contributions_element = soup.find("span", class_="ContributionCalendar-day")
                if contributions_element:
                    contributions = contributions_element["data-count"]
                    print(f"Contributions: {contributions}")
               
                print("\n")
                return
            raise ValueError("GitHub profile not found")
        except (requests.RequestException, ValueError) as e:
            print(f"[-] Error: {e}")

        input("\nPress any key to continue....")
        os.system("clear")
        banner()

def webcam_checker():
    # to search
    query = "inurl:'webcam xp 6'"

    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(j)

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
        print("  [2] Scan Google For Open Webcams")
        print("  [0] Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            input_string = input("[+] Enter a username: ")
            print(f'\n[+] Scanning for {input_string}...')
            print('-'*70)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for website in websites:
                    executor.submit(scan_website, website['url'], input_string)

            input("\nPress any key to continue....")
            os.system('clear')
            banner()
       
        elif choice == "2":
            print("\033[1;31m*** NOTE: if you get an error, please wait an hour and try again ***\033[0;37m")
            print("\033[1;32m[!] SCANNING FOR WEBCAMS\033[0;37m")
            webcam_checker()   
            input("\nPress any key to continue....")
            os.system('clear')  
            banner()    
        elif choice == "0":
            break
        else:
            print("\n[!] Invalid choice. Please try again.")
            input("\nPress any key to continue....")
            os.system('clear')
            banner()

if __name__ == "__main__":
    main()
