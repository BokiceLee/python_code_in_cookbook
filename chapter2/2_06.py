#字符串忽略大小写的搜索替换
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))#提供标志参数
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
#为了使替换的字符串大小写跟原来的字符串对应，借助辅助函数
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()#capitalize()方法
        else:
            return word
    return replace#返回了一个回调函数
re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)

