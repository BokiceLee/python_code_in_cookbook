#固定大小记录的文件迭代
from functools import partial
RECORD_SIZE=32
with open('somefile.txt','rt') as f:
    records=iter(partial(f.read,RECORD_SIZE),'')#iter特性，创建迭代器，一直调用可调用对象知道返回标记值
    for r in records:
        print('a:')
        print(r)