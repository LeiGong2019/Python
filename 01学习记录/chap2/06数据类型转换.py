# 在将不同数据类型的数据进行拼接的时候，就需要用到数据类型转换
name='张三'
age=20

print(type(name),type(age))
# name和age数据类型不一样

print('我叫'+name+',今年'+str(age)+'岁')
# age不能直接使用，否则会报错，提示类型转换；  转换成字符型就整除了
# str()，转义成字符串；   int()，转译成整数（文字和小数无法转）；   float()，转义成浮点数 （文字类无法转）

print(str(age),type(str(age)))
print(int(age),type(int(age)))
print(float(age),type(float(age)))

print(str(name),type(str(name)))
# print(int(name),type(int(name)))     会报错
# print(float(name),type(float(name)))  会报错

