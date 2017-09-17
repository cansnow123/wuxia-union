import datetime
import os

today = datetime.date.today()
dates = []
for i in range(0 - today.weekday(), 9 - today.weekday()):
    dates.append(today + datetime.timedelta(days=i))

# 掠夺、周六日盟会、周六帮派活动、周日醉侠
dir_list = [str(dates[0])+"掠夺", str(dates[1])+"掠夺", str(dates[2])+"掠夺", str(dates[3])+"掠夺", str(dates[4])+"掠夺",
            str(dates[5])+"盟会", str(dates[5])+"帮派活动", str(dates[6])+"盟会", str(dates[6])+"醉侠"]
code_ex = [x.encode('gbk')for x in dir_list]

print(code_ex)
for x in code_ex:
    if not os.path.exists(x):
        os.makedirs(x)
