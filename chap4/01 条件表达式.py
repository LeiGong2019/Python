num_a = int(input('please enter the first number:'))
num_b = int(input('please enter the second number:'))
# 比较大小
""" 
if num_a >= num_b:
    print(num_a, '大于等于', num_b)
else:
    print(num_a, '小于', num_b)
"""
print('使用条件表达式进行比较:')
print(str(num_a)+'大于等于'+str(num_b) if num_a >= num_b else str(num_a)+'小于'+str(num_b))
# if条件为true，执行左边； 否则执行右边；
