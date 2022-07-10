import matplotlib.pyplot as plt

plt.style.use('seaborn')

# 设置汉字格式，不然回出现乱码
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

# fig , ax = plt.subplots(nrows, ncols)，nrows 与 ncols 表示两个整数参数，它们指定子图所占的行数、列数。
# 创建了一个包含子图区域的画布，又创建了一个 figure 图形对象，
# 函数的返回值是一个元组，包括一个图形对象和所有的 axes 对象。其中 axes 对象的数量等于 nrows * ncols，且每个 axes 对象均可通过索引值访问（从1开始）。
fig, ax = plt.subplots()


x_values=range(1,1001)
y_valuse=[x**2 for x in x_values]
# scatter()方法，传递一对x和y坐标,点的尺寸大小为200，点颜色设置为红,也可以元组表示RGB； 还可以用颜色映射cmap，实现渐变色，
ax.scatter(x_values,y_valuse,c='red',s=1)

# 设置每个坐标轴的取值范围
ax.axis([0,1100,0,110000])

# 设置备注信息
# 通过方法set_title()设置标题
ax.set_title("标题：平方数",fontsize=12)
# 通过方法set_xlabel()设置x轴描述
ax.set_xlabel("x轴描述:值",fontsize=12)
# 通过方法
ax.set_ylabel("y轴描述:值的平方",fontsize=12)

# 设置刻度标记的大小，axis='both'表示对x，y轴都修改
ax.tick_params(axis='both',which='major',labelsize=14)

# 显示图片
plt.show()

# 也可以设置自动保存图表
# plt.savefig('squares_plot.png',bbox_inches='tight')
