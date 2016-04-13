import random
values=[1,2,3,4,5,6]
print(random.choice(values))
print(random.sample(values,2))#随机选取元素
random.shuffle(values)#打乱元素次序
print(values)
print(random.randint(0,10))
print(random.random())
#获取N位随机位(二进制)的整数
print(random.getrandbits(2))
#修改种子
random.seed()
print(random.random())