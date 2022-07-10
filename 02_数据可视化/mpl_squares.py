from tkinter import font
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

# 指定表格样式，模块里面有固定的模板，要放在指定汉字格式前面，不然会覆盖汉字设置，导致又出现中文乱码
plt.style.use('seaborn')

# 设置汉字格式，不然回出现乱码
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

input_values=[1,2,3,4,5]
squares = [1, 4, 9, 16, 25]



# 调用函数subplots,在一张图片中绘制一个或多个图表；fig，表示整张图片;ax，表示图片中的各个图表
fig, ax = plt.subplots()

# 调用plot()方法，指定x轴，y轴；尝试根据给定的数据以有意义的方式绘制图表;linewidth设置粗细;
ax.plot(input_values,squares,linewidth=3)

# 通过方法set_title()设置标题
ax.set_title("标题：平方数",fontsize=12)

# 通过方法set_xlabel()设置x轴描述
ax.set_xlabel("x轴描述:值",fontsize=12)

# 通过方法
ax.set_ylabel("y轴描述:值的平方",fontsize=12)

# 设置刻度标记的大小，axis='both'表示对x，y轴都修改
ax.tick_params(axis='both',labelsize=14)


# 函数plt.show()，打开Matplotlib查看并显示绘制的图表
plt.show()
