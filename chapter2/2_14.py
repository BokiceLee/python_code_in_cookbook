#合并拼接字符串
#合并序列或者iterable中的对象
parts=['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))

#简单的合并

print(parts[0]+' '+parts[1])#效率很低

print('Hello' 'World')

#仅在输出时的合并
print('Hello','World',sep='::')

#利用生成器产生输出片段
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago'
print(''.join(sample()))