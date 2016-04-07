#字符串开头或结尾匹配
import os
import re
from urllib.request import urlopen
filename='spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('spam'))
filenames=os.listdir('./')
li=[name for name in filenames if name.endswith(('1.py','2.py'))]#接受元组进行匹配
print(li)

def read_data(name):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices=['http:','ftp:']
url='http://www.python.org'
#url.startswith(choices)报错，只接受元组
print(url.startswith(tuple(choices)))

#可以使用切片来实现，但是很丑
filename='spam.txt'
print(filename[-4:]=='.txt')
print(url[:5]=='http:' or url[:6]=='https:' or url[:4]=='ftp:')
#也可以使用正则表达式
print(re.match('(http:)|(https:)|(ftps:)',url))

#最后可以通过前后缀 配合any关键字检查文件是否存在
