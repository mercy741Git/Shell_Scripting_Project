#!/bin/bash
# backup.sh — copy a file, with checks
file="$1"
if [ -z "$file" ]; then                # no argument?
  echo "Usage: $0 <file>"; exit 1
fi
if [ ! -f "$file" ]; then               # doesn't exist?
  echo "Error: $file not found"; exit 1
fi
cp "$file" "$file.bak"                   # do the backup
echo "Backed up $file at $(date +%T)"
