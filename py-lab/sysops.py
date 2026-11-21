import shutil, subprocess

# high-level file ops:
#shutil → for high-level file and directory operations.
shutil.copy2("logs/app.log", "logs/app.log.bak")   # copy
total, used, free = shutil.disk_usage("/")
print(f"disk: {used/total*100:.1f}% used, {free//(2**30)} GiB free")

# subprocess → for running external system commands and interacting with the operating system.
# run a system command safely (list of args, capture output):
'''r = subprocess.run(["df", "-h", "/"], capture_output=True, text=True, check=True)
print(r.stdout)
print("exit code:", r.returncode)'''