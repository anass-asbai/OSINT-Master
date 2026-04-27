import requests

def check_username(username):
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
    }

    results = {}

    headers = {"User-Agent": "Mozilla/5.0"}

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