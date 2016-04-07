#多个界定符分割字符串
import re
line='asdf fjdk;fafed, fjilaf,asdf, faf'
print(re.split(r'[;,\s]\s*',line))

fields=re.split(r'(;|,|\s)\s*',line)
print(fields)#包含括号捕获分组
#利用分隔符构造字符串
value=fields[::2]#步进
delimiters=fields[1::2]+['']
print(value)
print(delimiters)
print(''.join(v+d for v,d in zip(value,delimiters)))