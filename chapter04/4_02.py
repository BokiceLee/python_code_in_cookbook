#代理迭代
#在自定义容器对象上执行迭代操作
class Node:
    def __init__(self,value):
        self._value=value
        self._children=[]
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self,node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)#简单地将迭代请求传递给内部
if __name__=='__main__':
    root=Node(0)
    child1=Node(1)
    child2=Node(2)
    root.add_child(root)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)