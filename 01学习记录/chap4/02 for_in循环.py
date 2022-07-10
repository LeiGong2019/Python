for item in 'python':
    print(item)
#  第一次取出来的是p，将p赋值给item，将item输出；

# range()产生一个整数序列，也是一个可迭代对象；
for i in range(10):
    print(i)
# 输出 0~9

# 如果在循环体中不需要使用到自定义的变量，可将自定义变量写为"_"
for _ in range(5):
    print('python')
# 此时会输出5 遍 python；


print("使用for循环,计算1到100的偶数和")
sum = 0
for item in range(101):
    if not bool(item % 2):
        sum += item
print(sum)
