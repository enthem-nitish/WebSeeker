#!/bin/bash

echo "[*] WebSeeker Environment Setup for Kali Linux"
echo "[*] Developed by Nitish Sharma"

# System update
echo "[+] Updating system..."
sudo apt update && sudo apt upgrade -y

# Install dependencies
echo "[+] Installing required packages..."
sudo apt install python3 python3-pip python3-venv openjdk-17-jdk php git -y

# Create project directory
echo "[+] Creating WebSeeker directory..."
mkdir -p ~/WebSeeker/modules
cd ~/WebSeeker

# Create virtual environment
echo "[+] Creating Python virtual environment..."
python3 -m venv webseeker-env

# Activate virtual environment
source webseeker-env/bin/activate

# Create project files
echo "[+] Creating project structure..."
touch main.py config.py reporter.py requirements.txt targets.txt banner.sh
touch modules/__init__.py modules/xss_scanner.py modules/sqli_scanner.py 
touch modules/lfi_scanner.php modules/port_scanner.java

# Make banner executable
chmod +x banner.sh

# Install Python dependencies
echo "[+] Installing Python dependencies..."
echo "requests==2.31.0" > requirements.txt
pip install -r requirements.txt

echo "[+] Setup complete!"
echo "[+] To start using WebSeeker:"
echo "    cd ~/WebSeeker"
echo "    source webseeker-env/bin/activate"
echo "    python3 main.py"
