# 读取csv，显示最高温度

import csv

from matplotlib import pyplot as plt


#read() 函数：逐个字节或者字符读取文件中的内容； read()按输入参数size=a来读取从起始位置到a的所有字符，作为字符串保存在x里面
#readline() 函数：逐行读取文件中的内容； readline()则是死板的按行读取
#readlines() 函数：一次性读取文件中多行内容。 readlines输出的是列表
#reader()返回的值是csv文件中每行的列表




filename = '03_下载数据\data\sitka_weather_07-2018_simple.csv'
# 打开文件，并把它赋值给f，
with open(filename) as f:
    # 调用reader()函数，存储整个文件
    reader = csv.reader(f)
    # next(),返回文件中的下一行，这里只调用了一次，所以只是显示第一行
    header_row = next(reader)

    # 提取最高温度
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# 绘制温度表
plt.style.use('seaborn')

    # 设置汉字格式，不然回出现乱码
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题
fig,ax=plt.subplots()
ax.plot(highs,c='red')

ax.set_title('2018年7月每月最高稳定',fontsize=24)
ax.set_xlabel('',fontsize=16)
ax.set_ylabel('温度(F)',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()
