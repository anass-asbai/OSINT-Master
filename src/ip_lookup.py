import requests

def lookup_ip(ip_address):
    """Perform IP address lookup using ip-api.com."""
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        result = lookup_ip(sys.argv[1])
        print(result)
    else:
        print("Usage: python ip_lookup.py <ip_address>")
