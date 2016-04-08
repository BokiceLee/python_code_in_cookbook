#多行匹配模式
import re
text2= '''/* this is a
multiline comment */
'''
comment=re.compile(r'/\*((?:.|\n)*?)\*/')#指定一个非捕获组
print(comment.findall(text2))

#也可以使用标志参数使.匹配任意字符
comment=re.compile(r'/\*(.*?)\*/',re.DOTALL)
print(comment.findall(text2))
