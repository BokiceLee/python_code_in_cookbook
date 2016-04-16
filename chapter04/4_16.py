#迭代器代替while无限循环
li=[1,2,3,4,5]
i = -1
def get():
    global i
    i+=1
    return li[i]

for m in iter(get,3):
    print(m)