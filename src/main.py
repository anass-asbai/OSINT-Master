# src/main.py
import argparse
from ip_lookup import lookup_ip
from username_lookup import check_username
def main():
    parser = argparse.ArgumentParser(description="OSINT Tool")

    parser.add_argument("-i", "--ip", help="IP address to lookup")
    parser.add_argument("-u", "--username", help="Username to lookup")

    args = parser.parse_args()

    if args.username:
        result = check_username(args.username)
        print(result)
    if args.ip:
        result = lookup_ip(args.ip)
        print(result)

if __name__ == "__main__":
    main()