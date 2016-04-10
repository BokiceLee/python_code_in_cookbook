#在字符串中处理html和xml
import html
s = 'Elements are written as "<tag>text</tag>".'
print(s)
#替换'<','>'
print(html.escape(s))
# Disable escaping of quotes
print(html.escape(s, quote=False))
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))
t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))