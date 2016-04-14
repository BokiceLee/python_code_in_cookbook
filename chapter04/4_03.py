#使用生成器创建新的迭代模式
def frang(start,stop,increment):
    x=start
    while x<stop:
        yield '{:.1f}'.format(x)#format(x,'.1f')
        x+=increment
for n in frang(0,4,0.5):
    print(n)
print(list(frang(0,1,0.2)))
#生成器只能用于迭代操作

#底层
def countdown(n):
    print('Starting to count from ',n)
    while n>0:
        yield n
        n-=1
    print('Done')
c=countdown(3)
print(next(c))