
# 赋值运算符 ，运算顺序从右到左
i=3+4
print(i)


# 链式赋值
a=b=c=20  
print(a,id(a))
print(b,id(b))
print(c,id(c))
# 会发现，a,b,c 3个变量对应的内存地址，都一样


# 参数赋值
a=20
a+=30   # 相当于a=a+30
print(a)

# 系列解包赋值
a,b,c=10,20,30
print(a)
print(b)
print(c)


print ('------交换变量内容--------')
a=20
b=30
print('交换前:')
print(a,b)
a,b=b,a
print('交换后:\n',a,b)
