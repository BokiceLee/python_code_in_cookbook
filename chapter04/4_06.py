#带有外部状态的生成器函数
from collections import deque
class linehistory:
    def __init__(self,lines,histlen=3):
        self.lines=lines
        self.history=deque(maxlen=histlen)
    def __iter__(self):
        for lineno,line in enumerate(self.lines,1):#enumerate遍历的同时返回索引
            self.history.append((lineno,line))
            print(self.history)
            yield line
    def clear(self):
        self.history.clear()
with open('somefile.txt') as f:
    lines=linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno,hline in lines.history:
                print('{}:{}'.format(lineno,hline),end='')