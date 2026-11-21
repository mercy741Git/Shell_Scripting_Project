from pathlib import Path
import shutil

source_folder = Path("source")
backup_folder = Path("backups")

# Create the backup folder if it doesn't exist
backup_folder.mkdir(exist_ok=True)
    

# Copy all files from the source folder to the backup folder
'''for file in source_folder.iterdir(): #Current directory only
    if file.is_file() and file.suffix.lower() in [".log"]:
        shutil.copy2(file, backup_folder)'''

# Copy entire directory tree
'''shutil.copytree(
    source_folder,
    backup_folder / source_folder.name,
    dirs_exist_ok=True
)'''

# list out the all files based on the file extensions
files_by_ext = {}

# Current directory + all nested subdirectories (recursive) ->rglob
for file in source_folder.rglob("*"): 
    if file.is_file():
        ext = file.suffix or "NO_EXTENSION"

        #Creates a new list for the extension if it doesn't exist, and appends the file's name and full path to that list.
        files_by_ext.setdefault(ext, []).append({ #The code groups files by extension and stores each file's name and full path under that extension.
            "file": file.name,
            "path": str(file.resolve())
        })

with open("ListOfFiles.txt", "w") as f:       
    for ext, files in files_by_ext.items():
        f.write(f"\n{ext}:")
        for item in files:
            f.write(f"\n {item['file']} -> {item['path']}")

#print("Backup completed successfully.")