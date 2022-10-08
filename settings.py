class Settings(): #存储游戏所有设置的类
    """初始化游戏的静态设置"""
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800 # a.设置尺寸
        self.bg_color = (6, 2, 52) # b.设置背景色
        # 飞船设置
        self.ship_limit = 3 #飞船数量=3
        # 子弹设置
        self.bullet_width = 3 #宽3像素
        self.bullet_height = 15 #高15像素
        # self.bullet_color = 60, 60, 60 深灰色
        self.bullet_allowed = 3
        
        # 外星人子弹设置
        self.enemy_bullet_color = 230, 8, 0
        self.enemy_bullets_allowed = 5
        
        # 加快游戏的速度
        self.speedup_scale = 1.1
        # 加倍分数
        self.score_scale = 1.5

        #默认游戏难度为normal
        self.easy = False
        self.normal = True
        self.hard = False
    
    """初始化游戏的变化设置"""
    def initialize_dynamic_settings(self):
        self.fleet_direction = 1 # 外星人移动方向：向右（如果是-1，则向左）
        self.alien_points = 50 # 记分
        
        # 设置游戏不同等级难度
        if self.easy:
            self._easy_settings()
        elif self.normal:
            self._normal_settings()
        elif self.hard:
            self._hard_settings()
        
    def _easy_settings(self):
        # easy游戏难度的设置
        self.ship_speed_factor = 0.6
        self.bullet_color = (0, 0, 255)
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 8
        self.enemy_bullet_speed_factor = 0.3
        
    def _normal_settings(self):
        # normal游戏难度的设置
        self.ship_speed_factor = 0.8
        self.bullet_color = (234, 234, 234)
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.35
        self.fleet_drop_speed = 10
        self.enemy_bullet_speed_factor = 0.3
        
    def _hard_settings(self):
        # hard游戏难度的设置
        self.ship_speed_factor = 1
        self.bullet_color = (151, 235, 255)
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 12
        self.enemy_bullet_speed_factor = 0.3

    """提高速度和分数设置"""
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.enemy_bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        