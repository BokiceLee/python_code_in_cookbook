#结合时区的日期操作
from datetime import datetime,timedelta
from pytz import timezone,utc
d=datetime(2012,12,21,9,30,0)
print(d)

central=timezone('US/Central')
loc_d=central.localize(d)
print(loc_d)

bang_d=loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

d=datetime(2013,3,10,1,45)
loc_d=central.localize(d)
print(loc_d)
later=loc_d+timedelta(minutes=30)
print(later)

later=central.normalize(later)
print(later)

#转换为UTC
utc_d=loc_d.astimezone(utc)
print(utc_d)
later_utc=utc_d+timedelta(minutes=30)
print(later_utc.astimezone(central))

#查阅时区字典
from pytz import country_timezones
print(country_timezones['IN'])
for country,zone in country_timezones.items():
    print(country,zone)