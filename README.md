# HideAndSeek

A username OSINT tool that checks a list of websites for a matching profile, with optional "deep scan" lookups that pull extra profile details from supported platforms (GitHub, Reddit, Twitch, Steam, Pinterest, Ask.fm, Codecademy).

```
  ██░ ██  ██ ▓█████▄ ▓█████ ▄▄▄       ███▄    █ ▓█████▄   ██████ ▓█████ ▓█████  ██ ▄█▀
 ▓██░ ██▒▓██▒▒██▀ ██▌▓█   ▀▒████▄     ██ ▀█   █ ▒██▀ ██▌▒██    ▒ ▓█   ▀ ▓█   ▀  ██▄█▒ 
 ▒██▀▀██░▒██▒░██   █▌▒███  ▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌░ ▓██▄   ▒███   ▒███   ▓███▄░ 
 ░▓█ ░██ ░██░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌  ▒   ██▒▒▓█  ▄ ▒▓█  ▄ ▓██ █▄ 
 ░▓█▒░██▓░██░░▒████▓ ░▒████▒▓█   ▓██▒▒██░   ▓██░░▒████▓ ▒██████▒▒░▒████▒░▒████▒▒██▒ █▄
  ▒ ░░▒░▒░▓   ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░░ ▒░ ░▒ ▒▒ ▓▒
  ▒ ░▒░ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ ░ ░▒  ░ ░ ░ ░  ░ ░ ░  ░░ ░▒ ▒░
  ░  ░░ ░ ▒ ░ ░ ░  ░    ░    ░   ▒      ░   ░ ░  ░ ░  ░ ░  ░  ░     ░      ░   ░ ░░ ░ 
  ░  ░  ░ ░     ░       ░  ░     ░  ░         ░    ░          ░     ░  ░   ░  ░░  ░   
```

## Features

- **Username scanning** — checks a configurable list of sites (`websites` in `links.py`) to see if a profile exists for a given username.
- **Concurrent scanning** — uses a thread pool (capped at 10 workers) to check sites in parallel instead of one at a time.
- **Deep scan mode** (`-D`) — when a match is found on a supported platform, pulls extra profile details: display name, follower/following counts, bio info, etc.
- **Verbose mode** (`-v`) — also reports misses (no user found) and request errors, not just hits.
- **Graceful degradation** — missing page elements (changed site layouts) show `N/A` instead of crashing the scan.

## Supported deep-scan platforms

| Platform | Info gathered |
|---|---|
| GitHub | Username, location, website, followers, following, contributions |
| Reddit | Username, link karma, account creation date |
| Twitch | Followers, stream schedule |
| Steam | Steam ID, nickname, profile link |
| Pinterest | Name, username, followers, following |
| Ask.fm | Name, username, post count, like count |
| Codecademy | Username, activity status, course progress, badges, profile image |

## Requirements

- Python 3.8+
- [`requests`](https://pypi.org/project/requests/)
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/)
- [`praw`](https://pypi.org/project/praw/) (Reddit API)
- [`fake_useragent`](https://pypi.org/project/fake-useragent/) (optional — prompted for install on first run if missing)
- A `links.py` file in the same directory, exporting a `websites` list of `{"url": "..."}` dicts to check against.

Install dependencies:

```bash
pip install requests beautifulsoup4 praw fake_useragent
```

## API Credentials

Deep-scan lookups for Reddit and Twitch require API credentials. These must be set as **environment variables** — the script no longer accepts them hardcoded in source, and will skip those platforms with a warning if the variables aren't set.

```bash
export REDDIT_CLIENT_ID="your-reddit-client-id"
export REDDIT_CLIENT_SECRET="your-reddit-client-secret"
export TWITCH_CLIENT_ID="your-twitch-client-id"
export TWITCH_ACCESS_TOKEN="your-twitch-access-token"
```

- Reddit credentials come from a Reddit "script" app: https://www.reddit.com/prefs/apps
- Twitch credentials come from the Twitch Developer Console: https://dev.twitch.tv/console/apps

GitHub, Steam, Pinterest, Ask.fm, and Codecademy lookups scrape public pages directly and don't require credentials.

> **Security note:** if you were previously running a version of this script with credentials hardcoded in the source, treat those credentials as compromised and rotate them (regenerate the Reddit app secret and Twitch access token), especially if the code was ever committed to a public repo or shared anywhere.

## Usage

```bash
python hideandseek.py [-v] [-D]
```

### Arguments

| Flag | Long form | Description |
|------|-----------|--------------|
| `-v` | `--verbose` | Show misses and request errors in addition to hits. |
| `-D` | `--deep` | Enable deep scan — pulls extra profile details from supported platforms when a match is found. |

### Running it

```bash
python hideandseek.py -D -v
```

You'll get an interactive menu:

```
[1] Scan Websites For Username
[0] Exit
```

Choose `1` and enter a username to scan. Results print as they're found; with `-D` enabled, matches on supported platforms trigger an additional detailed lookup.

## How it works

1. Parses `-v`/`-D` flags and checks whether `fake_useragent` is installed (offers to install it if not).
2. Displays the banner and shows whether deep scan is enabled.
3. Prompts for a username, then submits one request per site in `links.py`'s `websites` list to a thread pool (max 10 concurrent).
4. For each site, if the username appears in the response and the status is `200`, it's reported as a match.
5. With `-D` enabled, a matched URL is checked against the supported platform list; if it matches one, the corresponding `Social` class method fetches and displays extra details.
6. With `-v` enabled, non-matches and request failures are also printed instead of silently skipped.

## Notes & Limitations

- Platform lookups scrape public HTML pages (GitHub, Steam, Pinterest, Ask.fm, Codecademy) — if those sites change their page structure, the corresponding fields will show `N/A` rather than crashing, but the extracted info may become stale until selectors are updated.
- The thread pool is capped at 10 concurrent workers to avoid hammering every listed site simultaneously; adjust `max_workers` in `scan_website()`'s `ThreadPoolExecutor` call if you need to tune this.
- All `requests.get()` calls use a 5-second timeout — slow or unresponsive sites will fail fast rather than hang the scan.

## Responsible use

This tool checks for *publicly visible* username matches across sites. Using it to compile profile data on individuals without their knowledge, for harassment, stalking, or unauthorized surveillance, is not an appropriate use — only run it against usernames you have a legitimate reason to look up (e.g. your own accounts, or OSINT work you're authorized to perform).

## Author

SwiftGlitxh
