import argparse
import json

from ip_lookup import lookup_ip
from username_lookup import check_username
from domain_enum import scan_domain


def save_output(data, file):
    try:
        with open(file, "w") as f:
            json.dump(data, f, indent=4)
        print(f"[+] Saved to {file}")
    except:
        print("[-] Save failed")


def main():
    parser = argparse.ArgumentParser(description="OSINT Tool")

    parser.add_argument("-i", "--ip")
    parser.add_argument("-u", "--username")
    parser.add_argument("-d", "--domain")
    parser.add_argument("-w", "--wordlist")
    parser.add_argument("-o", "--output")

    args = parser.parse_args()

    result = None

    if args.ip:
        print("[IP LOOKUP]")
        result = lookup_ip(args.ip)

    elif args.username:
        print("[USERNAME LOOKUP]")
        result = check_username(args.username)

    elif args.domain:
        print("[DOMAIN SCAN]")
        result = scan_domain(args.domain, args.wordlist)

    else:
        print("Usage: -i / -u / -d")
        return

    print(json.dumps(result, indent=4))

    if args.output:
        save_output(result, args.output)


if __name__ == "__main__":
    main()