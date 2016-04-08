#正则表达式中使用unicode
import re
num = re.compile('\d+')  #正则表达式中已提供对unicode码的支持，但是最好安装第三方正则库
# ASCII digits
print(num.match('123'))
# Arabic digits
print(num.match('\u0661\u0662\u0663'))