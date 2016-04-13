#矩阵与线性代数运算
import numpy as np
import numpy.linalg
m=np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(m)
#转置
print(m.T)
print(m.I)#?

v=np.matrix([[2],[3],[4]])
print(v)

#矩阵相乘
print(m*v)

#求det
print(numpy.linalg.det(m))

#solve for x in mx=v
print(numpy.linalg.solve(m,v))#求解
