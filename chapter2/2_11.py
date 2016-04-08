#删除字符串中的字符
import re
#Whitespace stripping
s = ' hello world \n'
print(s.strip())#默认去掉空白字符
print(s.lstrip())
print(s.rstrip())
# Character stripping
t = '-----  hel- lo  ====='
print(t.lstrip('-'))#去掉指定字符
print(t.strip('-= '))#不影响中间文本，只去头尾字符，需要用replace或正则表达式进行进一步处理
t=t.strip('-= ')
pat=re.compile('\s+|-+')
print(pat.sub('',t))
#创建生成器
pre=[' aew ','   af  ','aaf   ']
words = (word.strip() for word in pre)
for word in words:#创建了生成器words
    print(word)