from urllib import response
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"status code:{r.status_code}")

# 将数据信息转换为json字典
response_dict = r.json()

# 字典的get()方法，获取key对应的值
print(response_dict.keys())

# 输出字典中，total_count 键对应的值
print(f"Total repositories:{response_dict['total_count']}")

# 将'items'键对应的值，输入到 repo_dicts;'items'键对应的值，是一个列表
repo_dicts=response_dict['items']
# 输出列表长度，表示有多少拆仓库
print(f"Repositories returned: {len(repo_dicts)}")

# 这个repo_dicts列表的每一个元素都是一个字典,把第一个字典输入到repo_dict
repo_dict=repo_dicts[0]
print(f"\nkeys:{len(repo_dict)}")
print(repo_dict)

# 根据repo_dict字典中key进行排序
#for key in sorted(repo_dict.keys()):
#    print(key)
print('\nSelect information about each repository:')
for respo_dict in repo_dicts:
    print('\nName:',respo_dict['name'])
    print('Owner:',respo_dict['owner']['login'])
    print('Starts:',respo_dict['stargazers_count'])
    print('Repository:',respo_dict['html_url'])
    print('Description:',respo_dict['description'])
