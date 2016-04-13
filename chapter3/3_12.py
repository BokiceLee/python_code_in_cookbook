#基本日期与时间转换
from datetime import timedelta,datetime
a=timedelta(days=2,hours=6)
print(a)
b=timedelta(hours=4.5)
print(b)
print(a.days)
print(a.seconds)
print(a.total_seconds())
a=datetime(2012,9,23)
print(a)
now=datetime.today()
print(now)