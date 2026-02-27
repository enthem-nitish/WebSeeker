from datetime import datetime
from config import REPORT_FILE

class ReportGenerator:
    def __init__(self):
        self.findings = []

    def add_finding(self, target, module, result):
        self.findings.append({
            'target': target,
            'module': module,
            'result': result,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def generate_report(self):
        with open(REPORT_FILE, 'w') as f:
            f.write("WebSeeker Vulnerability Scan Report\n")
            f.write("Generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            f.write("Developed by Nitish Sharma\n")
            f.write("Support: https://t.me/supportBlackEnthembot\n")
            f.write("Instagram: @nitishraj2645\n")
            f.write("="*50 + "\n\n")

            for finding in self.findings:
                f.write(f"[Target] {finding['target']}\n")
                f.write(f"[Module] {finding['module']}\n")
                f.write(f"[Time] {finding['timestamp']}\n")
                f.write("[Findings]\n")
                f.write(finding['result'])
                f.write("\n" + "-"*50 + "\n\n")

        return REPORT_FILE
