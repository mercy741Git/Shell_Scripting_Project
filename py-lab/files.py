from pathlib import Path

# make a play directory with some files:
d = Path("logs"); d.mkdir(exist_ok=True)
(d / "app.log").write_text("line1\nline2\n")
(d / "error.log").write_text("boom\n")
(d / "notes.txt").write_text("ignore me\n")
print("exists?", d.exists(), "| dir?", d.is_dir())
for f in d.glob("*.log"):            # only .log files
    print(f.name, "->", f.stat().st_size, "bytes")
# read a file line by line:
with open(d / "app.log") as fh:
    for line in fh:
        print("read:", line.strip())