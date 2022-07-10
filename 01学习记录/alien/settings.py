class Settings:
    # 存储游戏《外星人入侵》中所有设置的类
    def __init__(self):

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        
        self.ship_limit=2

        # 子弹设置
        
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_allowed=10

        # alien
        
        self.fleet_drop_speed=10
        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()
        

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed=3.0
        self.alien_speed=0.5
        # 1标识右移，-1标识左移
        self.fleet_direction=1
        self.alien_points=50

    def increase_speed(self):
        self.ship_speed *=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
