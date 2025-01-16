from datetime import datetime

year1, month1, day1 = map(int, input().split())
year2, month2, day2 = map(int, input().split())

date1 = datetime(year1, month1, day1)
date2 = datetime(year2, month2, day2)

diff = date2 - date1
days = diff.days

if year2 - year1 > 1000 or (year2 - year1 == 1000 and (month2 > month1 or (month2 == month1 and day2 >= day1))):
    print("gg")
else:
    print(f"D-{days}")