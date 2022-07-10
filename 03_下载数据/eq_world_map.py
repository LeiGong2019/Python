from tokenize import cookie_re
from matplotlib.ft2font import LOAD_NO_SCALE
import plotly.express as px
from eq_explore_data import lons, lats,titles,mags
import pandas as pd

data =pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']
)
data.head()

# 
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    labels={'x': '经度', 'y': '维度'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
)

fig.write_html('global_earthquakes.html')
# 如果使用jupyter notebook,可以直接使用方法 fig.show(),此处测试使用vscode，无法使用此方法
# fig.show()

