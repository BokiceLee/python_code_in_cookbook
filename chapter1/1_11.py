###### ###0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)
SHARES = slice(20, 23,2)
print(record[SHARES])
PRICE = slice(31, 37,3)
print(record[PRICE])#slice(start,stop,step),创建切片对象，允许被用在任何允许切片的地方
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)
a=slice(5,50,2)
print(a.start)
print(a.step)
print(a.stop)
b=(1,2,4,5,6)
print(*b)#提取元组数值
s="HelloWorld"
a.indices(len(s))#自适应
for i in range(*a.indices(len(s))):
    print(s[i])