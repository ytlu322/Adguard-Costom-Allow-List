import re                       # 引入正表達式模組
from datetime import datetime   # 引入日期時間模組

file_path = "customrules.txt"   # 指定要處理的檔案名稱

# 以讀取模式開啟檔案，utf-8 編碼
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()       # 讀取所有行為串列

# 定義比對版本號的正則表達式樣式
version_pattern = re.compile(r"(! Version: )(\d+)\.(\d+)\.(\d+)\.(\d+)")
# 定義比對最後修改日期的正則表達式樣式
date_pattern = re.compile(r"(! Last modified: )(.+)")

# 逐行檢查檔案內容
for i, line in enumerate(lines):
    version_match = version_pattern.match(line)   # 嘗試比對版本號格式
    if version_match:
        major, minor, patch, build = map(int, version_match.groups()[1:]) # 取出四個數字並轉成整數
        build += 1                             # build 數字自動加一
        new_version = f"! Version: {major}.{minor}.{patch}.{build}"  # 組合成新版本字串
        lines[i] = new_version + "\n"          # 替換原本該列

    date_match = date_pattern.match(line)      # 嘗試比對日期格式
    if date_match:
        today = datetime.now().strftime("%Y-%m-%d")   # 取得今天日期 (YYYY-MM-DD)
        lines[i] = f"! Last modified: {today}\n"      # 更新為今天日期

# 以寫入模式覆蓋寫回整份檔案
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)                        # 將所有更新後的內容寫回檔案