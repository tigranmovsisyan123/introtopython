import datetime
import time
import calendar

print(datetime.datetime.today())
print(datetime.datetime.today().year)
print(datetime.datetime.today().month)
print(datetime.datetime.today().isoweekday())
print(datetime.datetime.today().weekday())
tdelta = datetime.timedelta(days=5)
tdelta2 =  datetime.timedelta(seconds=5)
print(datetime.datetime.today() - tdelta)
print(datetime.datetime.today() - tdelta2)
