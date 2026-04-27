# src/username_lookup.py
import requests

def check_username(username):
    sites = {
    # Main social networks
    "Facebook": f"https://www.facebook.com/{username}",
    "Twitter/X": f"https://twitter.com/{username}",
    "Instagram": f"https://www.instagram.com/{username}",
    "LinkedIn": f"https://www.linkedin.com/in/{username}",
    "Reddit": f"https://www.reddit.com/user/{username}",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Snapchat": f"https://www.snapchat.com/add/{username}",

    # Developer / tech platforms
    "GitHub": f"https://github.com/{username}",
    "GitLab": f"https://gitlab.com/{username}",
    "Bitbucket": f"https://bitbucket.org/{username}",
    "StackOverflow": f"https://stackoverflow.com/users/{username}",

    # Content / media platforms
    "YouTube": f"https://www.youtube.com/@{username}",
    "Twitch": f"https://www.twitch.tv/{username}",
    "Pinterest": f"https://www.pinterest.com/{username}",
    "Medium": f"https://medium.com/@{username}",
    "DevTo": f"https://dev.to/{username}",

    # Community / forums
    "Quora": f"https://www.quora.com/profile/{username}",
    "ProductHunt": f"https://www.producthunt.com/@{username}",
    "HackerNews": f"https://news.ycombinator.com/user?id={username}",

    # Gaming
    "Steam": f"https://steamcommunity.com/id/{username}",
    "Xbox": f"https://account.xbox.com/en-us/Profile?gamerTag={username}",
    "PlayStation": f"https://psnprofiles.com/{username}",

    # Art / design
    "Behance": f"https://www.behance.net/{username}",
    "Dribbble": f"https://dribbble.com/{username}",
    "DeviantArt": f"https://www.deviantart.com/{username}",

    # Writing / blogs
    "WordPress": f"https://{username}.wordpress.com",
    "Blogger": f"https://{username}.blogspot.com",

    # Misc / older networks
    "Tumblr": f"https://{username}.tumblr.com",
    "Flickr": f"https://www.flickr.com/people/{username}",
}

    results = {}

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for site, url in sites.items():
        try:
            r = requests.get(url, headers=headers, timeout=5)

            if r.status_code == 200:
                results[site] = "FOUND"
            else:
                results[site] = "NOT FOUND"

        except:
            results[site] = "ERROR"

    return results