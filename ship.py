import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """初始化飞船"""
    def __init__(self, ai_settings, screen):
        #调用super()继承精灵，以便创建飞船编组
        super(Ship, self).__init__()

        # 屏幕+设置
        self.screen = screen
        self.ai_settings = ai_settings

        # 外观：加载飞船图像，获取外接矩形
        self.image = pygame.image.load('image/ship.bmp') #返回飞船的surface
        self.rect = self.image.get_rect() #获取surface的属性rect
        self.screen_rect = screen.get_rect()
        
        # 初始位置：将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx #让矩形中心点处于屏幕中心点
        self.rect.bottom = self.screen_rect.bottom #让矩形底部与屏幕底部边缘对齐（top/bottom/left/right）
        
        # 在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动标志TF
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    """更新状态：根据移动标志调整位置+限制边缘"""
    def update(self):
        # 根据移动速度更新飞船的center坐标值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        
        # 根据self.center坐标值更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    """在屏幕上绘制飞船"""
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    """让飞船居中"""
    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)