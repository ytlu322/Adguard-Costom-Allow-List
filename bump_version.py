import re
from datetime import datetime

FILENAME = "customrules.txt"

with open(FILENAME, "r", encoding="utf-8") as f:
    lines = f.readlines()

today = datetime.now().strftime("%Y.%m.%d")
version_pattern = re.compile(r"^! Version: (\d{4})\.(\d{1,2})\.(\d{1,2})\.(\d+)")
last_modified_pattern = re.compile(r"^! Last modified: .*")

new_lines = []
bumped = False

for line in lines:
    # 處理 version
    m = version_pattern.match(line)
    if m:
        y, mth, d, n = m.groups()
        date_str = f"{y}.{int(mth)}.{int(d)}"
        if date_str == today:
            n = str(int(n) + 1)
        else:
            n = "1"
        new_version = f"! Version: {today}.{n}"
        new_lines.append(new_version + "\n")
        bumped = True
        continue
    # 處理 last modified
    if last_modified_pattern.match(line):
        new_lines.append(f"! Last modified: {datetime.now().strftime('%Y-%m-%d')}\n")
        continue
    new_lines.append(line)

if not bumped:
    # 若沒找到 version 行，則加在標頭後
    for idx, line in enumerate(new_lines):
        if line.startswith("! Description:"):
            new_lines.insert(idx + 1, f"! Version: {today}.1\n")
            break

with open(FILENAME, "w", encoding="utf-8") as f:
    f.writelines(new_lines)