#顺序迭代合并后的排序迭代对象
import heapq
a=[1,4,7,10]
b=[2,5,6,11]
#要求a、b预先排好序
for c in heapq.merge(a,b):
    print(c)