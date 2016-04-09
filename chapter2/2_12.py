#审查清理文本字符串
import unicodedata
import sys
s = 'pýtĥöñ\fis\tawesome\r\n'
#创建转换表格
remap={
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None,#这里的ord好像是必须的
}
a=s.translate(remap)
print(a)

cmb_chrs=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
print(cmb_chrs)
b=unicodedata.normalize('NFD',a)
print(b)
print(b.translate(cmb_chrs))

digitmap={c : ord('0')+unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c))=='Nd'}
print(digitmap)
print( '\u0661\u0662\u0663'.translate(digitmap))

b=unicodedata.normalize('NFD',a)
c=b.encode('ascii','ignore').decode('ascii')
print(c)

#使用str.replace处理简单字符是最快的，处理复杂字符则使用translate