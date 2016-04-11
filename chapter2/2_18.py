#字符串令牌解析
import re
from collections import namedtuple
text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ','='),
          ('NUM', '23'), ('PLUS','+'),
          ('NUM', '42'), ('TIMES', '*'),
          ('NUM', '10') ]
#定义所有可能的令牌
NAME=r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM=r'(?P<NUM>\d+)'
PLUS=r'(?P<PLUS>\+)'
TIMES=r'(?P<TIMES>\*)'
EQ=r'(?P<EQ>=)'
WS=r'(?P<WS>\s+)'
s='|'.join([NAME, NUM, PLUS, TIMES, EQ, WS])
print(s)
master_pat = re.compile(s)

scanner=master_pat.scanner(text)
#每次扫描匹配一个
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())

#打包成生成器
def generate_tokens(pat,text):
    Token=namedtuple('Token',['type','value'])
    scanner=pat.scanner(text)
    for m in iter(scanner.match,None):
        yield Token(m.lastgroup,m.group())

for tok in generate_tokens(master_pat,text):
    print(tok)

#令牌化使用的正则表达式需要指定所有输入中可能出现的文本序列，如果出现不匹配文本，扫描将直接停止
#令牌的顺序对扫描结果有影响，最好是长的模式写在前面