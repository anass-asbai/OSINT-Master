import socket

def load_wordlist(file_path=None):
    default = ["www", "mail", "ftp", "test", "dev", "api"]

    if file_path:
        try:
            with open(file_path, "r") as f:
                return [x.strip() for x in f if x.strip()]
        except:
            pass

    return default


def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return {"main_ip": ip}
    except:
        return {"main_ip": "Not resolved"}


def find_subdomains(domain, wordlist=None):
    subs = load_wordlist(wordlist)
    found = []

    for s in subs:
        full = f"{s}.{domain}"

        try:
            ip = socket.gethostbyname(full)
            found.append({"subdomain": full, "ip": ip})
        except:
            pass

    return found


def scan_domain(domain, wordlist=None):
    return {
        "main": resolve_domain(domain),
        "subdomains": find_subdomains(domain, wordlist)
    }