# OSINT Master Tool

## 📌 Overview

OSINT Master Tool is a lightweight but powerful Open Source Intelligence (OSINT) reconnaissance utility designed for educational and ethical cybersecurity learning purposes. It allows users to collect publicly available information about IP addresses, usernames, and domains using passive techniques.

This tool is intended to help learners understand how exposed information can be gathered from open sources and how attackers or security professionals analyze digital footprints.

---

## 🎯 Objectives

The main objectives of this project are:

* Learn OSINT methodologies used in cybersecurity
* Understand how public data can be collected and analyzed
* Practice Python programming in a real-world scenario
* Work with APIs, DNS queries, and HTTP requests
* Build modular and scalable security tools

---

## ⚙️ Features

### 1. IP Address Lookup

* Retrieves geolocation information
* Displays ISP / organization details
* Uses public IP information services

### 2. Username Reconnaissance

* Checks username existence across multiple platforms:

  * GitHub
  * Twitter / X
  * Instagram
  * Reddit
  * LinkedIn
* Determines whether a username is publicly registered

### 3. Domain & Subdomain Enumeration

* Resolves main domain IP address
* Performs subdomain brute-force using wordlists
* Supports custom wordlists
* Identifies active subdomains via DNS resolution

### 4. Output Export

* Saves results in structured JSON format
* Supports file-based reporting for further analysis

---

## 🧠 How It Works

The tool operates in three main phases:

1. **Input Handling**

   * User provides IP, username, or domain via CLI arguments

2. **Data Collection**

   * The tool sends requests to public services or performs DNS lookups

3. **Result Processing**

   * Responses are parsed and formatted into readable JSON output

4. **Storage (Optional)**

   * Results can be saved to a file for documentation or reporting

---

## 🧰 Installation

### Step 1: Clone or download the project

```bash
git clone https://github.com/anass-asbai/OSINT-Master
cd OSINT-Master
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 🔹 General Help

```bash
python3 src/main.py --help
```

---

### 🔹 IP Address Lookup

```bash
python3 src/main.py -i 8.8.8.8 -o output.json
```

Example output:

```json
{
  "ip": "8.8.8.8",
  "city": "Mountain View",
  "country": "US",
  "org": "Google LLC"
}
```

---

### 🔹 Username Search

```bash
python3 src/main.py -u johndoe -o user.json
```

Example output:

```json
{
  "GitHub": "FOUND",
  "Twitter": "NOT FOUND",
  "Instagram": "FOUND",
  "Reddit": "FOUND",
  "LinkedIn": "NOT FOUND"
}
```

---

### 🔹 Domain & Subdomain Enumeration

```bash
python3 src/main.py -d example.com -w wordlist.txt -o domain.json
```

Example output:

```json
{
  "main": {
    "main_ip": "93.184.216.34"
  },
  "subdomains": [
    {
      "subdomain": "www.example.com",
      "ip": "93.184.216.34"
    }
  ]
}
```

---

## 📁 Wordlist Support

The tool supports custom wordlists for subdomain enumeration.

Example `wordlist.txt`:

```
www
mail
ftp
test
dev
api
admin
vpn
staging
beta
cdn
```

You can load it using:

```bash
python3 src/main.py -d example.com -w wordlist.txt
```

---

## ⚠️ Ethical & Legal Notice

This tool is developed strictly for **educational and ethical cybersecurity purposes only**.

By using this tool, you agree that:

* You will only test systems you own or have permission to analyze
* You will not use this tool for malicious or illegal activities
* You understand the legal implications of OSINT and data collection

Unauthorized use of this tool is strictly discouraged.

---

## 🧱 Project Structure

```
osint-master/
│
├── src/
│   ├── main.py
│   ├── ip_lookup.py
│   ├── username_lookup.py
│   └── domain_enum.py
│
├── wordlist.txt
├── requirements.txt
└── README.md
```

---

## 🧠 Technical Concepts Used

* Python scripting
* REST APIs
* DNS resolution
* HTTP status code analysis
* File handling (JSON export)
* CLI argument parsing
* Modular programming

---

## 📌 Limitations

* Relies on public APIs (rate limits may apply)
* Subdomain detection is based on wordlist brute force only
* Username detection is based on public URL availability
* No advanced passive DNS or CT logs integration

---

## 🚀 Future Improvements

* Multithreading for faster scanning
* Integration with passive DNS APIs
* Certificate Transparency log scanning
* PDF report generation
* GUI interface for non-CLI users
* Database storage support

---

## 👨‍💻 Author

Cybersecurity Learning Project

---

## 🏁 Final Note

This project is designed to simulate real-world OSINT workflows in a simplified and educational manner. It helps learners understand how exposed information can be collected and how cybersecurity professionals think during reconnaissance phases.
