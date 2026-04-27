import socket

def load_wordlist(file_path=None):
    default = ["www", "mail", "ftp", "test", "dev", "api"]

    if file_path:
        try:
            with open(file_path, "r") as f:
                return [line.strip() for line in f if line.strip()]
        except:
            print("[!] Failed to load wordlist, using default")

    return default


def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return {"main_ip": ip}
    except:
        return {"main_ip": "Not resolved"}


def find_subdomains(domain, wordlist=None):
    subdomains = load_wordlist(wordlist)
    found = []

    for sub in subdomains:
        full = f"{sub}.{domain}"

        try:
            ip = socket.gethostbyname(full)

            found.append({
                "subdomain": full,
                "ip": ip
            })

        except:
            pass

    return found


def scan_domain(domain, wordlist=None):
    return {
        "main": resolve_domain(domain),
        "subdomains": find_subdomains(domain, wordlist)
    }