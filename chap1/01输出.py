# 可以输入数字
print(520)
print(98.5)

# 可以输出字符串
print('hello world !')
print("hello world !")

# 输出含有运算符的表达式
print(3+1)


# 将数据输出到文件
fp=open('D:/test.txt','a+')
print("hello world !",file=fp)
fp.close()
# 注意，windows目录，表示路径使用 "/"
# "a+",表示如果文件不存在就创建，如果存在，就在文件内容后面再追加


