#使用unicodedata模块标准化unicode文本
import unicodedata
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
t1=unicodedata.normalize('NFC',s1)#标准化为整体组成
t2=unicodedata.normalize('NFC',s2)
print(t1)
print(t2)
print(ascii(t1))
print(unicodedata.normalize('NFD',s1))#标准化为多个组合字符

s = '\ufb01'
print(s)

print(unicodedata.normalize('NFD',s))
print(unicodedata.normalize('NFKD',s))
print(unicodedata.normalize('NFKC',s))#不同标准对应什么应用场景？

t1=unicodedata.normalize('NFD',s1)
print(t1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
print(unicodedata.combining('̃'))#combining方法？

