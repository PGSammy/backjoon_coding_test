import datetime

def get_date(month, day):
    target_date = datetime.date(2007, month, day)
    return target_date.strftime('%A')[:3].upper()

month, day = map(int, input().split())

result = get_date(month, day)
print(result)