#跳过可迭代对象的开始部分
with open('somefile.txt') as f:
    lines =(line for line in f if not line.startswith('#'))
    for line in lines:
        print(line,end='')

#知道获取的元素的形式
from itertools import dropwhile
with open('somefile.txt') as f:
    for line in dropwhile(lambda line:line.startswith('#'),f):
        print(line,end='')
#明确知道所要获取的元素的索引
from itertools import islice
items = ['a','b','c',1,3,4,5]
for x in islice(items,3,None):
    print(x)