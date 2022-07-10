# 绘制随机漫步图
import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
# 设置屏幕尺寸为 15*9英寸；  屏幕分辨率是100像素/英寸
fig, ax = plt.subplots(figsize=(15,9))

#设置渐变色
point_numbers=range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues,s=5)

# 隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# 突出起点和终点
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
plt.show()
