#字符串搜索和替换
import re
from calendar import month_abbr
text = 'yeah, but no, but yeah, but no, but yeah'
text=text.replace('yeah', 'yep')
print(text)
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
#text=re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))
#用替换回调函数代替模式串
def change_date(m):#回调函数的参数为m
    mon_name=month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mon_name,m.group(3))
datepat.sub(change_date,text)

#另外可获取替换数
newtext,n=datepat.subn(r'\3-\1-\2',text)
print(newtext,n)