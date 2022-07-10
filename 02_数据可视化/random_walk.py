from random import choice

class RandomWalk:
    def __init__(self,num_points=5000):
        # 初始化随机漫步的属性
        self.num_points=num_points

        # 初始默认值
        self.x_values=[0]
        self.y_values=[0]

    def fill_walk(self):
        # 设置随机次数
        while len(self.x_values) < self.num_points:
            # 设置随机方向，1和-1
            x_direction=choice([1,-1])
            # 设置随机距离
            x_distination=choice([0,1,2,3,4])
            # 计算出应该朝哪个方向移动多少距离
            x_step=x_direction*x_distination

            y_direction=choice([1,-1])
            y_distination=choice([0,1,2,3,4])
            y_step=y_direction*y_distination
            
            # 设置拒绝原地踏步，如果是原地踏步，直接略过记录
            if x_step == 0 and y_step==0:
                continue
            # 根据计算的x，y坐标移动的方向距离，和上一个点的坐标，一起计算出当前点的坐标
            x=self.x_values[-1]+x_step
            y=self.y_values[-1]+y_step

            # 将所有的x，y坐标，放入一个列表；
            self.x_values.append(x)
            self.y_values.append(y)