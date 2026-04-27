# src/domain_enum.py
import dns.resolver
import socket

def resolve_domain(domain):
    result = {}

    try:
        ip = socket.gethostbyname(domain)
        result["main_ip"] = ip
    except:
        result["main_ip"] = "Not resolved"

    return result


def find_subdomains(domain):
    
    subdomains = ["www", "mail", "ftp", "test", "dev", "api","learn","blog","shop","support","portal","admin","beta","staging"]
    
    found = []

    for sub in subdomains:
        full_domain = f"{sub}.{domain}"

        try:
            ip = socket.gethostbyname(full_domain)
            found.append({
                "subdomain": full_domain,
                "ip": ip
            })
        except:
            pass

    return found


def scan_domain(domain):
    return {
        "main": resolve_domain(domain),
        "subdomains": find_subdomains(domain)
    }