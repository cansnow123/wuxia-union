import pytz
import datetime
tz = pytz.timezone('Asia/Hong_Kong')
bj = datetime.datetime.now(tz)
a_st = bj.strftime("%Y/%m/%d")

print(bj)

dates = []
for i in range(0 - bj.weekday(), 9 - bj.weekday()):
    dates.append(bj + datetime.timedelta(days=i))
weekdays = []
for x in range(7):
    weekdays.append(dates[x].strftime("%Y/%m/%d"))
print("本周日期：", weekdays)