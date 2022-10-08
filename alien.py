import pygame
from pygame.sprite import Sprite

class Alien(Sprite): 
    """初始化外星人"""
    def __init__(self, ai_settings, screen):
        #调用super()继承精灵
        super(Alien, self).__init__()

        # 屏幕+设置
        self.screen = screen
        self.ai_settings = ai_settings

        # 外观：加载外星人图像，获取外接矩形
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect() #设置图片的rect属性

        # 初始位置：每个外星人都在屏幕顶部左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确横坐标
        self.x = float(self.rect.x) 
    
    """位置标志：检查外星人群是否位于屏幕边缘"""
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right -10:
            return True 
        elif self.rect.left <= 10:
            return True
    
    """更新状态：向左或向右移动"""
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x #更新横坐标

    """在屏幕上绘制外星人"""
    def blitme(self):
        self.screen.blit(self.image, self.rect)
