# import pytz
# import datetime
# tz = pytz.timezone('Asia/Hong_Kong')
# bj = datetime.datetime.now(tz)
# a_st = bj.strftime("%Y/%m/%d")
#
# print(bj)
#
# dates = []
# for i in range(0 - bj.weekday(), 9 - bj.weekday()):
#     dates.append(bj + datetime.timedelta(days=i))
# weekdays = []
# for x in range(7):
#     weekdays.append(dates[x].strftime("%Y/%m/%d"))
# print("本周日期：", weekdays)
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("test@chr.moe")
to_email = Email("hf.heiybb@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)