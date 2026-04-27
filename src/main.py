import argparse

from ip_lookup import lookup_ip
from username_lookup import check_username
from domain_enum import scan_domain


def main():
    parser = argparse.ArgumentParser(description="OSINT Master Tool")

    parser.add_argument("-i", "--ip", help="IP address lookup")
    parser.add_argument("-u", "--username", help="Username search")
    parser.add_argument("-d", "--domain", help="Domain scan")
    parser.add_argument("-w", "--wordlist", help="Custom subdomain wordlist")

    args = parser.parse_args()

    if args.ip:
        print("[IP INFO]")
        print(lookup_ip(args.ip))

    elif args.username:
        print("[USERNAME INFO]")
        print(check_username(args.username))

    elif args.domain:
        print("[DOMAIN INFO]")
        print(scan_domain(args.domain, args.wordlist))

    else:
        print("Use --help for options")


if __name__ == "__main__":
    main()