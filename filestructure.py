from pathlib import Path

folders= ["logs", "backups", "reports", "configs","deployments"]

for folder in folders:

    Path(folder).mkdir(exist_ok=True)

    print(f"Folder '{folder}' created successfully.")

print("All folders created successfully.")
