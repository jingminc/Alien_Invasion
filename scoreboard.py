import pygame.font
from pygame.sprite import Group
from ship import Ship
# 显示得分信息
class Scoreboard():
    """初始化显示得分涉及的属性"""
    def __init__(self, ai_settings, screen, stats):
        # 需要跟踪的值
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # 字体及颜色
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # 准备当前得分图像和最高分图像
        self.prep_score() 
        self.prep_high_score()
        self.prep_level()
        # 准备可供显示的飞船编组
        self.prep_ships()

    """将文本转化为图像"""
    def prep_score(self):
        # 文本
        rounded_score = int(round(self.stats.score, -1)) # round()-调整到10的整数倍
        score_str = "{:,}".format(rounded_score)
        # 渲染
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
        # 创建矩形
        self.score_rect = self.score_image.get_rect()
        # 位置：屏幕右上角
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20 
    
    def prep_high_score(self):
        # 文本
        high_score = int(round(self.stats.high_score, -1)) # 从game_state获得分数
        high_score_str = "{:,}".format(high_score)
        # 渲染
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.ai_settings.bg_color) 
        # 创建矩形
        self.high_score_rect = self.high_score_image.get_rect() 
        # 位置：屏幕顶部中央
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top 

    def prep_level(self):
        # 渲染
        self.level_image = self.font.render(str(self.stats.level), True,
                self.text_color, self.ai_settings.bg_color)
        # 创建矩形
        self.level_rect = self.level_image.get_rect()
        # 位置：放在得分下方
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self): #显示还剩多少飞船
        self.ships = Group() #空编组
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen) # 创建新飞船
            ship.rect.x = 10 + ship_number * ship.rect.width # 设置横坐标：让飞船编组位于屏幕左边
            ship.rect.y = 10 # 设置纵坐标：距离屏幕上边缘
            self.ships.add(ship)

    """在屏幕上绘制分数、最高分、等级、剩余飞船"""
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect) 
        self.ships.draw(self.screen) 