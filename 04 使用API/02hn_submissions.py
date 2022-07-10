# 这种引用方式，就不要加 openrator.xxx 了； 一般不建议，容易造成名字冲突
from operator import itemgetter

import requests

# 这个json文件中，是一串id号
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status Code:{r.status_code}")

submission_ids = r.json()
submission_dicts = []

# 遍历所有id
for submission_id in submission_ids:
    url=f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    # 获取每个id对应的文章
    r=requests.get(url)
    print(f"id:{submission_id}\tstatus:{r.status_code}")
    # 将文章数据转换为字典
    response_dict=r.json()

    # 将每篇文章转换为字典，再把字典存储到列表 submission_dicts
    submission_dict={
        'title':response_dict['title'],
        'hn_link':f"https://hacker-news.firebaseio.com/v0/item/?id={submission_id}",
        'comments':response_dict['descendants'],
    }

    submission_dicts.append(submission_dict)

# 对列表里面的内容进行排序，基于评论
submission_dicts=sorted(submission_dicts,key=itemgetter('comments'),reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle:{submission_dict['title']}")
    print(f"Discussion link:{submission_dict['hn_link']}")
    print(f"Comments:{submission_dict['comments']}")
