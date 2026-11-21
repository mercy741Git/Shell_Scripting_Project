import time, os
from datetime import datetime

def is_stale(path, days=7):
    """Return True if the file is older than `days` days."""
    # Full date and time
    mod_time = os.path.getmtime(path)
    dt = datetime.fromtimestamp(mod_time)
    print(dt)

    # Date only (YYYY-MM-DD)
    #print(dt.date())
    print(f"days: {dt.date()}")
    age_seconds = time.time() - os.path.getmtime(path)
    return age_seconds > days * 86400
def greet(name: str) -> str:        # type hints
    return f"hi {name}"
# make a test file, then call the function:
open("demo.txt", "w").close()
print(is_stale("demo.txt"))          # False (just created)
print(is_stale("demo.txt", days=0))  # True  (older than 0 days)
print(greet("DevOps49"))             # hi DevOps49

