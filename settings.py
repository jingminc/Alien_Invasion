class Settings(): #存储游戏所有设置的类
    """初始化游戏的静态设置"""
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1440
        self.screen_height = 800 # a.设置尺寸
        self.bg_color = (6, 2, 52) # b.设置背景色
        # 外星人设置
        self.ship_size = (120, 80)
        self.alien_density_factor_x = 2.2
        self.alien_density_factor_y = 2

        # 飞船设置
        self.ship_size = (120, 80)
        self.ship_limit = 2 #飞船数量
        self.score_ship_size = (60, 40)
        
        # 子弹设置
        self.bullet_width = 4 #宽3像素
        self.bullet_height = 15 #高15像素
        # self.bullet_color = 60, 60, 60 深灰色
        self.bullet_allowed = 3
        
        # 外星人子弹设置
        self.enemy_bullet_color = 230, 8, 0
        
        # 加快游戏的速度
        self.speedup_scale = 1.3
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
        self.ship_speed_factor = 0.8
        self.bullet_color = (234, 234, 234)
        self.bullet_speed_factor = 1.2
        self.alien_speed_factor = 0.4
        self.fleet_drop_speed = 10
        self.enemy_bullet_speed_factor = 0.3
        self.enemy_bullets_allowed = 2
        
    def _normal_settings(self):
        # normal游戏难度的设置
        self.ship_speed_factor = 0.8
        self.bullet_color = (151, 235, 255)
        self.bullet_speed_factor = 1.2
        self.alien_speed_factor = 0.4
        self.fleet_drop_speed = 13
        self.enemy_bullet_speed_factor = 0.3
        self.enemy_bullets_allowed = 4
        
    def _hard_settings(self):
        # hard游戏难度的设置
        self.ship_speed_factor = 1
        self.bullet_color = (151, 235, 255)
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor = 0.6
        self.fleet_drop_speed = 16
        self.enemy_bullet_speed_factor = 0.3
        self.enemy_bullets_allowed = 4

    """提高速度和分数设置"""
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.enemy_bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        