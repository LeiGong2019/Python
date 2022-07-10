from tkinter import N


a=3.1415926
print(a,type(a))

n1=1.1
n2=2.2
print(n1+n2,'\n')
# 会发现，两数相加值不精确，为3.3000000000000003； 是因为计算机是采用二进制存储的，浮点数的存储会存在一定误差；
# 解决方法是导入模块decimal 来计算浮点数的运算

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
