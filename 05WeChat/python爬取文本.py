""" 
    File Name:      爬取笔趣阁.py   笔趣阁:https://www.xbiquge.so/
    Description:    爬虫
    module:         requests,lxml
    note:      

    模块介绍：
        requests库: python的第三方包,用来做接口测试,接口自动化测试,爬虫；
        lxml库:     解析和提取html中的数据
"""

import requests        # 导入http库
from lxml import etree     # 导入lxml解析库


url = "http://www.xbiquge.so/book/55136/"           # 设置一个url变量，变量为url地址
req = requests.get(url)  # 申请地址数据；  requests直接把整个页面数据申请到，放到内存了；
list_page = etree.HTML(req.text)      # 解析数据，用于操作
txt_name = list_page.xpath("//h1/text()")[0]    # 获取书名；  其中xpath怎么使用，可以百度学习，//是匹配的所有
file_name = f'./{txt_name}.txt'           # 定义本地存储名称
list_a = list_page.xpath("//dd/a//@href")[12:]   # 提取所有章节页; //@href,是选取所有名为 href 的所有属性；
list_a = [url + i for i in list_a]         # 拼接所有章节页完整链接
for i in list_a:       # 循环所有章节页
    req = requests.get(i)       # 申请章节页数据
    data_page = etree.HTML(req.text)        # 解析整个页面的数据
    data_title  = data_page.xpath("//h1/text()")[0]  # 提取章节页名称
    print(data_title)
    data_list = data_page.xpath("//div[@id='content']/text()")[1:]           # //title[@lang],表示获取所有拥有名为lang的属性的title元素
    data = "\n".join(data_list)     # 拼接小说内容
    this_chapter = f"\n{data_title}\n{data}"  #拼接标题与内容
    with open(file=file_name,mode="a",encoding='UTF-8') as f:       #本地新建文件
        f.write(this_chapter)       #将小说内容写入文件
    print(f'{data_title}---下载完成!')   # 打印下载
