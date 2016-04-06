#合并多个字典或映射
from collections import ChainMap
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c=ChainMap(a,b)#有优先级的区别,#逻辑上合并，内部并没有合并
print(c['x'],c['y'],c['z'])
print(len(c))
print(list(c.keys()))
print(list(c.items()))
print(list(c.values()))
#更新或删除操作只是影响第一个字典中的值
#del(c['y']) 此语句报错s


values = ChainMap()#神奇的new_child和parent方法
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
print(values)

#字典的等价实现,需要创建新的字典或者破坏原有的字典
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
print(b)
b.update(a)

#字典实现：对元素值的修改不会映射到合成字典中，而ChaiMap实现可以映射
merge=ChainMap(a,b)
a['x']=8
print(b)
print(merge)