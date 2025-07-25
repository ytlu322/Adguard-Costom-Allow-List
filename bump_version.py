import re
from datetime import datetime

file_path = "customrules.txt"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

version_pattern = re.compile(r"(! Version: )(\d+)\.(\d+)\.(\d+)\.(\d+)")
date_pattern = re.compile(r"(! Last modified: )(.+)")

for i, line in enumerate(lines):
    version_match = version_pattern.match(line)
    if version_match:
        major, minor, patch, build = map(int, version_match.groups()[1:])
        build += 1
        new_version = f"! Version: {major}.{minor}.{patch}.{build}"
        lines[i] = new_version + "\n"
    date_match = date_pattern.match(line)
    if date_match:
        today = datetime.now().strftime("%Y-%m-%d")
        lines[i] = f"! Last modified: {today}\n"

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)
