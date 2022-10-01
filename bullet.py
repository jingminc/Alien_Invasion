import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): #精灵可以同时操作编组中所有元素
    """初始化子弹"""
    def __init__(self, ai_settings, screen, ship): #创建实例
        #调用super()继承精灵
        super(Bullet, self).__init__() 

        # 屏幕
        self.screen = screen
        # 外观：在（0，0）处创建一个表示子弹的矩形
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # 初始位置：飞船顶部
        self.rect.centerx = ship.rect.centerx #起始横坐标：飞船的横坐标
        self.rect.top = ship.rect.top #起始纵坐标：飞船矩形的顶部

        # 子弹纵坐标用小数表示
        self.y = float(self.rect.y)
        # 颜色
        self.color = ai_settings.bullet_color  
        # 速度
        self.speed_factor = ai_settings.bullet_speed_factor 
    
    """更新状态：向上移动子弹"""
    def update(self):
        # 纵坐标 = 纵坐标-移动速度
        self.y -= self.speed_factor
        # 矩形位置 = 纵坐标
        self.rect.y = self.y
    
    """在屏幕上绘制子弹"""
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)