#精确的浮点运算
from decimal import Decimal,localcontext
a= Decimal('12.323')
b=Decimal('43.12')
print(a+b)
#创建本地上下文，控制计算的每一个方面
with localcontext( ) as ctx:
    ctx.prec=3
    print(a/b)
