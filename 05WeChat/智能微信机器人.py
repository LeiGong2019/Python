import requests
# 导入控件控制库；  uiautomation是一个windows自动化控制工具，安装：pip install uiautomation
import uiautomation as ui
# pyperclip，剪切板相关库，可以将字符串复制到剪切板或读取剪切板内容； 安装：pip install pyperclip
import pyperclip

# 绑定名为微信的主窗口控件
wx = ui.WindowControl(Name='微信')
# 切换窗口,会调出微信
wx.SwitchToThisWindow()
# 寻找会话控件绑定
hw=wx.ListControl(Name='会话')

while True:
    we=hw.TextControl(searchDepth=4)   # 查找未读消息
    try:
        if we.Name:   # 假如存在未读消息
            we.Click(simulateMove=False)   #点击未读消息
            last_msg=wx.ListControl(Name='消息').GetChildren()[-1].Name  # 读取最后一条消息
            response=requests.get(f"http://api.qingyunke.com/api.php?key=free&appid=0&msg={last_msg}")  # 智能接口
            msg=response.json()['content']    # 结果提取
            pyperclip.copy(msg.replace('{br}','\n'))  # 替换接口中的换行符
            wx.SendKeys("{Ctrl}v",waitTime=0) # 将结果输入文本框
            wx.SendKeys("{Enter}",waitTime=0)  # 回车发送消息
            wx.TextControl(SubName=msg[:5]).RightClick()    # 通过消息匹配检索会话栏中的联系人并右击
            ment=ui.MenuControl(ClassName="CMenuWnd")      # 匹配右击控件
            ment.TextControl(Name="不显示聊天").Click()    # 点击右击控件中的不显示聊天
    except:
        pass