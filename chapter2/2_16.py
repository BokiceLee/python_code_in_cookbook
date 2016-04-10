#指定列宽格式化字符串
import textwrap
import os
s = "Look into my eyes, look into my eyes, the eyes, the eyes," \
    "the eyes, not around the eyes, don't look around the eyes, " \
    "look into my eyes, you're under."
print(s)
print(textwrap.fill(s,width=40,initial_indent='****'))
print(textwrap.fill(s,width=50,subsequent_indent='####'))
#print(os.get_terminal_size().columns)#获取终端大小