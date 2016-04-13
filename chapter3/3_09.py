#大型数组运算
import numpy as np
ax=np.array([1,2,3,4])
ay=np.array([5,6,7,8])
print(ax*2)
print(ax+10)
print(ax+ay)
print(ax*ay)
#该模块还提供通用函数
print(np.sqrt(ax))
print(np.cos(ax))

#构造超大数组
grid=np.zeros(shape=(10000,10000),dtype=int)
print(grid)
#同样所有操作都会作用到每个元素
print(grid+10)


#numpy扩展了列表的索引功能
a=np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
#选择某行
print(a[1])
#选择某列
print(a[:,2])

#选择子矩阵
print(a[1:3, 1:3])
#按行加
print(a+[100,101,102,103])
#条件操作
print(np.where(a<10,a,10))