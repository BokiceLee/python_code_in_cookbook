#字节字符串的字符串操作
import re
#支持正则表达式，正则表达式本身必须是字节串
data=b'a a'
#print(re.split('\s',data))报错
print(re.split(b'\s',data))

#注意
#1、字节字符串的索引操作返回的是整数而非字符
#2、字节字符串的输出需要先解码为文本字符串,否则无法支持格式化操作
print(data.decode('ascii'))