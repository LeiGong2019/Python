from unittest import result
from urllib.parse import _ResultMixinBytes

from plotly.graph_objs import Bar,Layout
from plotly import offline

from die import Die

die = Die()
results = []
#投掷100次
for roll_num in range(1001):
    result = die.roll()
    # 结果放在resultes()列表中
    results.append(result)

frequencies=[]
# 记录骰子每个面出现的次数
for value in range(1,die.num_sizes+1):
    # 记录某一个面出现的次数
    frequency=results.count(value)
    # 每个面次数放到 frequencies列表中；
    frequencies.append(frequency)

# 绘制直方图
x_values=list(range(1,die.num_sizes+1))
#设置坐标轴范围
data=[Bar(x=x_values,y=frequencies)]

#X轴的描述
x_axis_config={'title':'结果'}

# y轴的描述
y_axis_config={'title':'结果的频率'}

# 指定图表布局
my_layout=Layout(title='掷一个D6 1000次的结果',xaxis=x_axis_config,yaxis=y_axis_config)

# offline.plot()，包含数据，布局对象的字典，和文件名
offline.plot({'data':data,'layout':my_layout},filename='d6.html')

