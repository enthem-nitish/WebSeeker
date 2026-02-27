#!/usr/bin/env python3
import os
import subprocess
import sys
from config import TARGET_FILE, JAVA_CLASS_PATH
from reporter import ReportGenerator

def display_banner():
    # Run the banner script
    script_path = os.path.join(os.path.dirname(__file__), 'banner.sh')
    subprocess.run([script_path], check=True)

def load_targets():
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Target file '{TARGET_FILE}' not found.")
        sys.exit(1)
    with open(TARGET_FILE, 'r') as f:
        targets = [line.strip() for line in f if line.strip()]
    return targets

def run_module(module_name, target):
    """Runs a specific scanning module against a target."""
    try:
        if module_name.endswith('.py'):
            # Run Python module
            result = subprocess.run([sys.executable, f"modules/{module_name}", target],
                                   capture_output=True, text=True, timeout=120)
            return result.stdout
        elif module_name.endswith('.java'):
            # Compile and Run Java module
            class_name = module_name.replace('.java', '')
            subprocess.run(['javac', f"modules/{module_name}", '-d', 'modules/'], check=True, timeout=30)
            result = subprocess.run(['java', '-cp', JAVA_CLASS_PATH, class_name, target],
                                   capture_output=True, text=True, timeout=120)
            return result.stdout
        elif module_name.endswith('.php'):
            # Run PHP module
            result = subprocess.run(['php', f"modules/{module_name}", target],
                                   capture_output=True, text=True, timeout=120)
            return result.stdout
    except subprocess.TimeoutExpired:
        return f"[!] Module {module_name} timed out for {target}"
    except Exception as e:
        return f"[!] Error running {module_name}: {str(e)}"
    return ""

def main():
    display_banner()

    targets = load_targets()
    if not targets:
        print("[!] No targets found in targets.txt")
        return

    # Define the modules to run (in order)
    modules_to_run = [
        'port_scanner.java',
        'xss_scanner.py',
        'sqli_scanner.py',
        'lfi_scanner.php'
    ]

    report_gen = ReportGenerator()

    for target in targets:
        print(f"\n[*] Scanning target: {target}")
        for module in modules_to_run:
            print(f"    [>] Running {module}...")
            findings = run_module(module, target)
            if findings:
                report_gen.add_finding(target, module, findings)

    # Generate the final report
    report_path = report_gen.generate_report()
    print(f"\n[+] Scan complete! Report saved to: {report_path}")

if __name__ == "__main__":
    main()
