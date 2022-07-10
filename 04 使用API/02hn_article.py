from urllib import response
import requests
import json

# url类型为str
url='https://hacker-news.firebaseio.com/v0/item/19155826.json'
# 请求获取内容，r的类型为requests.models.Response
r=requests.get(url)
print(f"Status Code:{r.status_code}")

# 将内容转换为字典
response_dict=r.json()
# readable_file，类型为str
readable_file=r'04 使用API\data\readable_eq_data.json'
with open(readable_file,'w') as f:
    json.dump(response_dict,f,indent=4)
