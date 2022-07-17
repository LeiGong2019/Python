""" 
内容：      淘宝秒杀测试， 采用selenium 模块
使用模块：  Selenium是一个用于web应用程序测试的工具， Selenium测试直接运行在浏览器中， 就像真正的用户在操作一样；
额外安装：   pip install selenium     
            pip install datetime
            下载webdriver，下载网址： https://registry.npmmirror.com/binary.html?path=chromedriver/
            
                注意：安装完成后，Selenium需要配合webdriver才能使用，webdriver下载放置在任意非中文路径的文件夹下即可；
                注意：选择一个和浏览器版本契合或最近的文件； 如chorme是101.0.4951.54，修改浏览器快捷方式中的目标，添加 --remote-debugging-port=6001
"""


# 导入驱动
from numpy import datetime_data
from selenium import webdriver
# 导入驱动服务
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # 导入By包进行元素定位
import time
import datetime

from selenium.webdriver.support.ui import WebDriverWait  # 导入web驱动等待服务
from selenium.webdriver.support import expected_conditions as EC  # 导入条件预设组件

# 驱动服务指定路径，路径指向chromedriver.exe
s = Service(r"05WeChat\chromedriver.exe")
options = webdriver.ChromeOptions()   # 谷歌浏览器选项
options.add_experimental_option("debuggerAddress", "127.0.0.1:6001")  # 添加以debug模式启动的谷歌浏览器
driver = webdriver.Chrome(options=options,service=s)  # 初始化浏览器服务
driver.get('https://cart.taobao.com/cart.htm')  # 打开网址，  已提前web打开登录好淘宝账号
time.sleep(2)  # 等待2s，页面加载完成

driver.find_element(By.ID,"J_SelectAll1").click()   # 选中ID属性点击，这里点击的是全选
time.sleep(2)  # 等待2s，页面加载完成；  是因为自己电脑"结算"按键刷新太慢，要等待
ti= '2022.7.17 01:16:00' #设置一个时间
startTime = datetime.datetime.strptime(ti,'%Y.%m.%d %H:%M:%S')  #时间格式转化
while datetime.datetime.now() < startTime:
    print(datetime.datetime.now())
    print('时间等待中：%s' % datetime.datetime.now()) # 输出时间
    time.sleep(0.01) #设置时间等待，用于精确时间
print("时间到了，开始抢购")
# 选择ID属性进行点击，这里点击的是结算;   选中页面的 “结算”，右键  insepct
driver.find_element(By.ID,"J_Go").click()       
# 点击提交订单，获取元素时间，每0.1秒检测一下，是否可以检测到获取到订单属性，检测到后立刻提交
WebDriverWait(driver,5,0.1).until(EC.presence_of_element_located((By.LINK_TEXT,"提交订单"))).click()
