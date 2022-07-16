import datetime
print(datetime.datetime.now())

ti= '2022.7.12 02:50:10' #设置一个时间
startTime = datetime.datetime.strptime(ti,'%Y.%m.%d %H:%M:%S')  #时间格式转化
print(startTime)
print (datetime.datetime.now() < startTime)