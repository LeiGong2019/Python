# 输入函数

present=input('大圣想要什么礼物呢？')
# 大圣想要什么礼物呢 ， 是提示语句
print(present,type(present))


# 但是input的结果是个 字符串类型，str
a=input("请输入一个加数：")  # 输入10
b=input('请输入另一个加数：') # 输入20
print(a+b)
#会发现，输入值 1020，不是数值的相加，因此此时a,b都是str类型

print(type(a),type(b))
print(int(a)+int(b))
