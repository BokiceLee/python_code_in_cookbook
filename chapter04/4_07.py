#迭代器切片
def count(n):
    while True:
        yield n
        n+=1
c=count(0)
#c无法通过下标切片,通过itertools在迭代器或者生成器上做切片
import itertools
for x in itertools.islice(c,10,20):
    print(x)
#消耗性！
