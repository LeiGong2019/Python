# 使用plotly模拟掷骰子

from random import randint


class Die:
    # 如果Die()不指定面数，骰子默认6个面
    def __init__(self, num_sizes=6):
        self.num_sizes = num_sizes


    def roll(self):
        # 返回一个1和骰子面数之间的随机值
        return randint(1, self.num_sizes)
