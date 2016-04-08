#字符串匹配和搜索
import re
#简单字面匹配
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.find('but',8,9))#返回第一个关键字

#复杂匹配使用正则表达式
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
if re.match(r'\d+/\d+/\d+',text1):
    print("1")
if re.match(r'\d+/\d+/\d+',text2):
    print("2")

#编译模式对象
datepat=re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print("3")
if datepat.match(text2):
    print("4")
#match 总是从字符串开始处匹配，不一定完全匹配
#findall寻找所有匹配字符串
text= 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))
#利用括号捕获分组
datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
m=datepat.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(datepat.findall(text))
#返回迭代结果
for m in datepat.finditer(text):
    print(m.groups())