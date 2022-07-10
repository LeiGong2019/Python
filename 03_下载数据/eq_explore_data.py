# 提取震级

import json

# from matplotlib.pyplot import title

filename = '03_下载数据\data\eq_data_30_day_m1.json'
with open(filename) as f:
    # 读取json，并存储为字典
    all_eq_data = json.load(f)

# 提取 features相关的数据
all_eq_dicts = all_eq_data['features']

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])
