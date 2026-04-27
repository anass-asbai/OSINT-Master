# OSINT Master

A modular Open Source Intelligence (OSINT) tool for performing IP lookups, username checks, and domain enumeration.

## Features
- **IP Lookup**: Retrieve information about an IP address using ip-api.com
- **Username Lookup**: Check if a username exists on common platforms (GitHub, Twitter, Reddit)
- **Domain Enumeration**: Perform basic DNS lookups for a domain

## Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd osint-master
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main entry point:
```bash
python src/main.py --help
```

### Examples
- Lookup an IP address:
  ```bash
  python src/main.py ip 8.8.8.8
  ```
- Check a username:
  ```bash
  python src/main.py username john_doe
  ```
- Enumerate a domain:
  ```bash
  python src/main.py domain example.com
  ```

## Testing
Run tests with pytest:
```bash
pytest tests/
```

## Project Structure
```
osint-master/
├── src/               # Source code modules
├── tests/             # Test files
├── output/            # Directory for storing results
├── resources/         # Project resources (e.g., images)
├── README.md          # Project documentation
├── requirements.txt   # Python dependencies
└── .gitignore         # Git ignore rules
```
