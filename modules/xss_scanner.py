import sys
import requests

def test_xss(url, payload):
    try:
        # For GET parameters
        r = requests.get(url, params={"q": payload}, timeout=5)
        if payload in r.text:
            return True
    except requests.exceptions.RequestException:
        pass
    return False

def main():
    if len(sys.argv) < 2:
        print("[!] Usage: python xss_scanner.py <target_url>")
        sys.exit(1)

    target_url = sys.argv[1]
    payloads = ['<script>alert("XSS")</script>', '"><script>alert("XSS")</script>', 'javascript:alert("XSS")']

    print(f"[*] Testing for Reflected XSS on: {target_url}")
    vulnerable = False
    for payload in payloads:
        if test_xss(target_url, payload):
            print(f"[!] Potential XSS found with payload: {payload}")
            vulnerable = True

    if not vulnerable:
        print("[-] No basic reflected XSS vulnerabilities found.")

if __name__ == "__main__":
    main()
