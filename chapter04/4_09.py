#组合排列的迭代
items=['a','b','c']
#排列
from itertools import permutations
for p in permutations(items):
    print(p)
#传递可选参数
for p in permutations(items,2):
    print(p)

#组合
from itertools import combinations
for c in combinations(items,3):
    print(c)
for c in combinations(items,2):
    print(c)

#允许多次选择
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items,3):
    print(c)