#测试文件或目录是否存在
import os
print(os.path.exists('.\somefile.txt'))
print(os.path.isdir('.\somefile.txt'))

import time
print(time.ctime(os.path.getmtime('.\somefile.txt')))