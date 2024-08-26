from datetime import datetime

# 입사일 설정
join_date = datetime(2021, 4, 12)

# 현재 날짜와 비교
now = datetime.now()
diff = (now.year - join_date.year) * 12 + now.month - join_date.month + 2

# README.md 파일 열기
with open("README.md", "r") as f:
    lines = f.readlines()

# "2021.04 ~ now (" 라인 찾기
for i, line in enumerate(lines):
    if "2021.04 ~ now" in line:
        # 개월 수 업데이트
        lines[i] = f"  2021.04 ~ now ({diff} months)\n"

# README.md 파일 저장
with open("README.md", "w") as f:
    f.writelines(lines)
