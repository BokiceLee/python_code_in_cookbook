#文件不存在才能写入
#使用x模式
import os
#print(os.path)
if not os.path.exists('somefile.txt'):
    with open('somefile.txt','xt') as f:
        f.write('good')
else:
    print('exist')