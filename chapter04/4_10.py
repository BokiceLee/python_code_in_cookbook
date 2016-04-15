#序列上索引值迭代
#迭代一个序列的同时跟踪一个正在被处理的元素索引
my_list=['a','b','c']
for idx,val in enumerate(my_list):
    print(idx,val)
#传递开始参数
for idx,val in enumerate(my_list,1):
    print(idx,val)

from collections import defaultdict
word_summary=defaultdict(list)
with open('somefile.txt') as f:
    lines=f.readline()
print(lines)
for idx,line in enumerate(lines):
    words=[w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)
print(word_summary)