# 斐波那契数是指 每个数是前两个数之和

fibs=[0,1]
a=int(input('please enter how many fibonacci numbers do you want?'))
for i in range(a):
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)