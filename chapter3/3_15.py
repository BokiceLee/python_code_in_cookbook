#字符串转换为日期
from datetime import datetime
text='2012-09-20'
#拆开
y=datetime.strptime(text,'%Y-%m-%d')
z=datetime.now()
print(z-y)
z=datetime(2013,9,23)
#合并
nice_z=datetime.strftime(z,'%A %B %d,%Y')
print(nice_z)
