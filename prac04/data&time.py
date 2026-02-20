#1
import datetime
now = datetime.datetime.now()
print(now)
#2
import datetime
date = datetime.date(2025, 3, 15)
print(date)
#3
import datetime
now = datetime.datetime.now()
print(now.strftime("%d.%m.%Y %H:%M"))
#4
import datetime
d1 = datetime.date(2025, 3, 1)
d2 = datetime.date(2025, 3, 10)
print((d2 - d1).days)
#5
import datetime
utc_time = datetime.datetime.now(datetime.timezone.utc)
print(utc_time)