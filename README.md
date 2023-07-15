# HIDEANDSEEK (beta V0.8) 
![hideandseekv0 8](https://github.com/swiftglitxh/hideandseek/assets/72777943/9c9c8d2d-5981-44c4-8ec2-3fc2d80a7846)

## 👓 What is HideAndSeek?

This tool is called "HideAndSeek." It is a Python script that allows you to scan multiple websites for a specific username. The script takes a username as input and searches for its presence on various platforms or websites. It uses the `requests` library to send HTTP requests to each website and checks if the username exists in the response.

The script supports the following features:

1. Verbose Mode: You can enable verbose output to see detailed information about the scanning process, including websites that are down or where the username was not found.

2. Silent Mode: You can enable silent mode to suppress the output and only save the results to a file.

3. Output File: You can specify an output file path where the results will be saved.

4. User-Agent Spoofing: The script uses the `fake_useragent` library (if installed) to generate random user agents for each request, which helps in disguising the requests and avoiding detection.

The script utilizes multithreading with the `concurrent.futures.ThreadPoolExecutor` to perform parallel scanning of multiple websites, making the scanning process faster.

Please note that the accuracy of the results depends on the availability and correctness of the platforms or websites being scanned.
### 👀 Hideandseek scans many known platforms, such as:
HideAndSeek scans various popular websites for the presence of a specific username. While the exact list of websites may vary depending on the specific implementation of the script, here are some examples of popular sites that are commonly included:
- Facebook
- Twitter
- Instagram
- LinkedIn
- GitHub
- Reddit
- Pinterest
- Tumblr
- Snapchat
- TikTok
  
Please note that the availability and accuracy of the results for each website can vary and may depend on factors such as the website's API, search functionality, and privacy settings.

## ⌨️ Commands
1. -v or --verbose: This command enables verbose mode, which provides detailed information about the scanning process. It displays additional output, such as websites that are down or where the username was not found.

2. -o FILE or --output FILE: This command specifies an output file path where the results of the scan will be saved. Instead of printing the results to the console, they will be written to the specified file.

3. -s or --silent: This command enables silent mode, which suppresses the output on the console. Only the results will be saved to the output file, if specified.
HideAndSeek Flags
'''
options:
  -h, --help  show this help message and exit
  -v          Verbose
  -o FILE, --output FILE' Output file path
  -s, --silent' Silent mode
]

## UPDATES 0.8

The recent updates to the script include the following:

`1` More websites have been added into the `links.py` 
`2` `-D/--deep` argument has been added. 
`3` Scraping websites such as `twitch` `github` `Steam` and more 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🎥 Example 
```
you@pc: hideandseek.py
[=]  Enter a username:  swiftglitxh
[!]  Scanning 'swiftglitxh' on 121 different platforms

[+] [FOUND]  https://www.ravelry.com/people/7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://reddit.com/user/7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://www.shutterfly.com/sitesearch/7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://www.plurk.com/7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://imgur.com/search?q=7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://skyrock.com/search/articles/?q=7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://www.instagram.com/7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://www.quora.com/search?q=7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://youtube.com/c/7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://www.virgin.com/profile/7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://www.codecademy.com/profiles/7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://www.namasha.com/search?q=7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://steamcommunity.com/id/7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://in.pinterest.com/7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://www.calm.com/profile/7NEWSSpotlight  =>  7NEWSSpotlight Found!
[+] [FOUND]  https://www.kw.com/kw/7NEWSSpotlight  =>  7NEWSSpotlight Found!
...           
[!] SCAN COMPLETE!
```

## 📚 Langauges & Libraries Used
![python](https://img.shields.io/badge/Language-Python-blue?logo=icloud&color=white&logoColor=white)&nbsp;&nbsp;![python](https://img.shields.io/badge/Library-Requests-blue?logo=BookStack&logoColor=white)&nbsp;&nbsp;![python](https://img.shields.io/badge/Library-Argparse-red?logo=BookStack&logoColor=white)
