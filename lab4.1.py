#Python date
#1
import datetime
today = datetime.datetime.now()
five_days_ago = today - datetime.timedelta(days=5)
print(f"Five days ago: {five_days_ago}")

#2
import datetime
from datetime import timedelta
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + timedelta(days = 1)

print(f"Yesterday:  {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")

#3
now = datetime.datetime.now()
now_without_microsec = now.replace(microsecond=0)
print(now_without_microsec)

#4
date1Str = input("Enter 1st date in format 'dd.mm.YYYY hh.mm.ss' : ")
date2Str = input("Enter 2nd date in format 'dd.mm.YYYY hh.mm.ss' : ")

date1 = datetime.strptime(date1Str, "%d.%m.%Y %H:%M:%S")
date2 = datetime.strptime(date2Str, "%d.%m.%Y %H:%M:%S")

diffInSec = abs((date1 - date2).total_seconds())
print(f"{diffInSec} seconds")