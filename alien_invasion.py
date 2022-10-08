import sys
import pygame
from settings import Settings
from game_state import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf
from button import Button
from pygame.sprite import Group 

def run_game():
    """初始化设置"""
    pygame.init()
    ai_settings = Settings() #使用设置模块，储存在ai_settings中
    # 创建窗口 pygame.display.set_mode
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) 
    pygame.display.set_caption("Alien Invasion") #设置当前窗口标题
    # 创建Play按钮
    play_button = Button(ai_settings, screen, 'Play')

    # 飞船实例
    ship = Ship(ai_settings, screen) #使用飞船模块
    # 子弹实例
    bullets = Group() #创建用于存储子弹的空编组
    enemy_bullets = Group()
    # 外星人实例
    aliens = Group() #创建用于存储外星人的空编组
    gf.create_fleet(ai_settings, screen, ship, aliens) #创建外星人群
    # 游戏统计实例
    stats = GameStats(ai_settings)
    # 记分实例 
    sb = Scoreboard(ai_settings, screen, stats)
    
    """开始游戏的主循环"""
    while True:
        # 监视键盘和鼠标
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, enemy_bullets)

        # 更新状态
        if stats.game_active:
            # 更新飞船：位置
            ship.update()
            # 更新子弹：位置+删除
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 更新外星人子弹
            gf.update_enemy_bullets(ai_settings, screen, stats, sb, ship, aliens, enemy_bullets)
            # 更新外星人：与子弹撞、与飞船撞
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, enemy_bullets)

        # 每次循环时都重绘屏幕（飞船、外星人、子弹、按钮）
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, enemy_bullets) 

run_game()
