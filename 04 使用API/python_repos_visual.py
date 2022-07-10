from numpy import append
import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"status code:{r.status_code}")

# 处理结果
# 将数据信息转换为json字典
response_dict = r.json()
# 将'items'键对应的值，输入到 repo_dicts;'items'键对应的值，是一个列表
repo_dicts = response_dict['items']

# 创建空列表
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
#    repo_names.append(repo_dict['name'])
    repo_name=repo_dict['name']
    repo_url=repo_dict['html_url']
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    
    # stargazers_count , 观星者数量
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# 可视化,定义列表data
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'},
    },
    'opacity': 0.6,
}]
# my_layout字典
my_layout = {
    'title': 'GibHub上最受欢迎的Python项目',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
