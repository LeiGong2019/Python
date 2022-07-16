import requests
# 导入控件控制库；  uiautomation是一个windows自动化控制工具，安装：pip install uiautomation
import uiautomation
# pyperclip，剪切板相关库，可以将字符串复制到剪切板或读取剪切板内容； 安装：pip install pyperclip
import pyperclip

# 定义程序窗口
uiautomation.WindowControl(Name='WeChat')
# 切到到程序窗口
uiautomation.WindowControl(Name='WeChat').SwitchToThisWindow()

