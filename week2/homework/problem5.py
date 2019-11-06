import datetime
import time
import calendar

bday = datetime.date(1996,11,25)
print(bday)
print(bday.year)
print(bday.month)
print(bday.day)
print(bday.weekday())
tday = datetime.date.today()
bday2019 =  datetime.date(2019,11,25)
tillbday = bday2019 - tday 
print(tillbday)
print(calendar.month(2017,5))
tdelta = datetime.timedelta(days = -1)
yesterday = tday + tdelta
print(yesterday)
tdelta2 = datetime.timedelta(days = 2)
tdelta3 = datetime.timedelta(days = -3)
print(yesterday + tdelta2)
print(yesterday + tdelta3)