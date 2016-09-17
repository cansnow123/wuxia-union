import datetime
import os

date1 = datetime.datetime.now()

this_mon = str(date1-datetime.timedelta(days=date1.weekday())).split()[0]
this_tue = str(date1-datetime.timedelta(days=9-date1.weekday())).split()[0]
this_wed = str(date1-datetime.timedelta(days=8-date1.weekday())).split()[0]
this_thu = str(date1-datetime.timedelta(days=7-date1.weekday())).split()[0]
this_fir = str(date1+datetime.timedelta(days=4-date1.weekday())).split()[0]

wk_list = [this_mon, this_tue, this_wed, this_thu, this_fir]
dir_list = [x+"掠夺" for x in wk_list]

for x in dir_list:
    if not os.path.exists(x):
        os.makedirs(x)
