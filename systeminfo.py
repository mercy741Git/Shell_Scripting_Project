import os 
import sys
import subprocess
import platform
from pathlib import Path

import psutil

computer_name = platform.node()
#print(f"Computer Name: {computer_name}")

os_name = platform.system()
#print(f"Operating System: {os_name}")

os_version = platform.version()

# Device Name
#print("Device Name:", platform.node())

# Processor
#print("Processor:", platform.processor())

# RAM
ram_gb = psutil.virtual_memory().total / (1024**3)
#print(f"Installed RAM: {ram_gb:.1f} GB")

# System Type
arch = platform.architecture()[0]
machine = platform.machine()
#print(f"System Type: {arch}, {machine}")

# Storage
disk = psutil.disk_usage('C:\\')
used = disk.used / (1024**3)
total = disk.total / (1024**3)
#print(f"Storage: {used:.0f} GB of {total:.0f} GB used")

# Graphics Card (Windows)
gpu = subprocess.check_output(
    'wmic path win32_VideoController get name',
    shell=True
).decode(errors='ignore').split('\n')[1].strip()

#print("Graphics Card:", gpu)
#print(f"OS Version: {os_version}")
with open("system_info.txt", "w") as f:
    f.write(f"Computer Name: {computer_name}\n")
    f.write(f"Operating System: {os_name}\n")
    f.write(f"OS Version: {os_version}\n")
    f.write(f"Processor:  {platform.processor}\n")
    f.write(f"Installed RAM: {ram_gb:.1f} GB\n")
    f.write(f"System Type: {arch}, {machine}\n")
    f.write(f"Storage: {used:.0f} GB of {total:.0f} GB used\n")
    f.write(f"Graphics Card: {gpu}\n")
        
print("Information saved to system_info.txt")
