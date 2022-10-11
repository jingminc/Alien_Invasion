import pygame.font
class Button():
    """初始化按钮"""
    def __init__(self, ai_settings, screen, msg):
        # 屏幕
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # 基本属性:按钮尺寸
        self.width, self.height = 200, 60
        # 其他属性：背景颜色、文本颜色、字体
        self.button_color = (50, 206, 24)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font('font\joystix.monospace-regular.ttf', 42) # None是默认字体，48是字号
        
        # 外观：创建矩形
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # 初始位置：居中
        self.rect.center = self.screen_rect.center

        # 初始文本图像
        self.prep_msg(msg) 
    
    """将文本转化图像"""
    def prep_msg(self, msg): #self-实参，msg-文本
        # 渲染
        self.msg_image = self.font.render(msg, True, self.text_color, 
            self.button_color) #font.render()-将meg中的文本转换为图像；True-开启反锯齿功能
        # 创建文本图像的矩形
        self.msg_image_rect = self.msg_image.get_rect() 
        # 位置：在按钮上居中
        self.msg_image_rect.center = self.rect.center
    
    """绘制按钮和文本"""
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect) # 按钮 = 颜色填充至矩形
        self.screen.blit(self.msg_image, self.msg_image_rect) #传递一副图像及相关的rect对象