import sys
import pygame
from bullet import Bullet
from bullet import Enemy_Bullet
from alien import Alien
from time import sleep 
import random
        
"""响应按键和鼠标事件"""
def check_events(ai_settings, screen, stats,sb, play_button, ship, aliens,
        bullets, enemy_bullets):
    for event in pygame.event.get():# event是用户操作（鼠标/按键）
            if event.type == pygame.QUIT: #如果事件是游戏窗口的关闭按钮
                filename = 'highscore.txt'
                with open(filename, 'w') as file_object:
                    file_object.write(str(stats.high_score))
                sys.exit() # 退出游戏
            elif event.type == pygame.MOUSEBUTTONDOWN: #鼠标点击
                mouse_x, mouse_y = pygame.mouse.get_pos() #获取单机时鼠标的x,y坐标
                check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                    aliens, bullets, mouse_x, mouse_y, enemy_bullets) # 调用按钮函数
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, stats,sb, ship, aliens,
        bullets, enemy_bullets) #调用按下函数
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship) #调用松开函数

# 按下按键=True(移动) 移动飞船+创造子弹
def check_keydown_events(event,ai_settings, screen, stats,sb, ship, aliens,
        bullets, enemy_bullets):
    # 1）向右移动飞船
    if event.key == pygame.K_RIGHT: 
        ship.moving_right = True
    # 2）向左移动飞船
    if event.key == pygame.K_LEFT: 
        ship.moving_left = True
    # 3）向上移动飞船
    if event.key == pygame.K_UP: 
        ship.moving_up = True
    # 4）向下移动飞船
    if event.key == pygame.K_DOWN: 
        ship.moving_down = True
    # 5）空格键创造子弹
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets) 
    # 6）'q'退出游戏
    elif event.key == pygame.K_q:
        filename = 'highscore.txt'
        with open(filename, 'w') as file_object:
            file_object.write(str(stats.high_score))
        sys.exit()
    # 7）'p'或'Enter'键开始游戏
    elif event.key == pygame.K_p or event.key == pygame.K_RETURN:
        start_game(ai_settings, screen, stats, sb, ship, aliens,
        bullets, enemy_bullets)
    # 8）#在游戏停止的情况下，按e、n、h键调整游戏的难度
    elif event.key == pygame.K_e and not stats.game_active:
        ai_settings.easy = True
        ai_settings.normal = False
        ai_settings.hard = False
    elif event.key == pygame.K_n and not stats.game_active:
        ai_settings.easy = False
        ai_settings.normal = True
        ai_settings.hard = False
    elif event.key == pygame.K_h and not stats.game_active:
        ai_settings.easy = False
        ai_settings.normal = False
        ai_settings.hard = True

# 松开按键=False(停止) elif event.type == pygame.KEYUP: 
def check_keyup_events(event,ship):
    # 1）向右移动飞船
    if event.key == pygame.K_RIGHT: 
        ship.moving_right = False
    # 2）向左移动飞船
    if event.key == pygame.K_LEFT: 
        ship.moving_left = False
    # 3）向上移动飞船
    if event.key == pygame.K_UP: 
        ship.moving_up = False
    # 4）向下移动飞船
    if event.key == pygame.K_DOWN: 
        ship.moving_down = False   

# 按下Play按钮 = 开始游戏
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
        bullets, mouse_x, mouse_y, enemy_bullets):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) #检查鼠标的单击位置是否在按钮的rect内
    if button_clicked and not stats.game_active: # 点击按钮位置时游戏须为非活动状态
        start_game(ai_settings, screen, stats, sb, ship, aliens,
        bullets, enemy_bullets)

def start_game(ai_settings, screen, stats, sb, ship, aliens,
        bullets, enemy_bullets):
    # 激活游戏
    stats.game_active = True
    # 重置游戏
    ai_settings.initialize_dynamic_settings()
    # 隐藏光标
    pygame.mouse.set_visible(False) 
    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True
    # 重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
    sb.show_score()
    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()
    enemy_bullets.empty()
    # 创建一群新的外星人并让飞船居中
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship() 


"""更新屏幕"""
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
        play_button, enemy_bullets): 
    # 绘制屏幕
    screen.fill(ai_settings.bg_color) 
    # 绘制子弹
    for bullet in bullets.sprites(): #列表包含编组bullets中所有精灵
        bullet.draw_bullet() 
    # 绘制飞船 
    ship.blitme() 
    # 绘制外星人
    aliens.draw(screen) # 对编组调用draw，pygame自动绘制编组的每个元素（在屏幕上）
    # 绘制计分板
    sb.show_score()
    # 绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    
    if stats.game_active:	
        for enemy_bullet in enemy_bullets.sprites():
            enemy_bullet.draw_enemy_bullet()
        
        if random.randrange(0, 65) == 1:
            alien_shoot(ai_settings, screen, aliens, enemy_bullets)
        
        pygame.sprite.groupcollide(bullets, enemy_bullets, True, True)

    
    # 让最近绘制的屏幕可见
    pygame.display.flip() 

"""创建子弹"""
def fire_bullet(ai_settings, screen, ship, bullets): 
        if len(bullets) < ai_settings.bullet_allowed:
            #创建一颗子弹
            new_bullet = Bullet(ai_settings,screen,ship) 
            #将子弹加入Bullets编组中
            bullets.add(new_bullet)  

"""创造外星人子弹"""
def alien_shoot(ai_settings, screen, aliens, enemy_bullets):
	if len(enemy_bullets) < ai_settings.enemy_bullets_allowed:
		new_bullet = Enemy_Bullet(ai_settings, screen, aliens)
		enemy_bullets.add(new_bullet)

# 检查是否诞生新的最高分
def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score() 

# 写入最高分
def load_score(stats):
	filename = 'highscore.txt'
	try:
		with open(filename) as file_object:
			score = file_object.read()
			stats.high_score = int(score)
	except FileNotFoundError:
		pass

# 检查子弹是否击中外星人，如果是，就删除相应的子弹和外星人
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):            
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) #遍历bullets和aliens

    # 记分
    if collisions:
        # 发出撞击音效
        pygame.mixer.init()
        pygame.mixer.music.load('sound\8177.wav')
        pygame.mixer.music.play()
        # 在字典collisions中：与外星人碰撞的子弹是键，而与每颗子弹相关的值是列表，包含撞到的外星人
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb) 

    # 外星人=0时（处理）
    if len(aliens) == 0:
        bullets.empty() # 删除现有子弹
        ai_settings.increase_speed() # 加快游戏
        
        stats.level += 1
        sb.prep_level() #提高等级

        create_fleet(ai_settings, screen, ship, aliens) # 新建一群外星人
        

# 状态更新：移动+删除子弹
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 更新子弹位置
    bullets.update()
    # 删除子弹: 触顶【简单事件】
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 调函数：与外星人碰撞【复杂事件】
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def update_enemy_bullets(ai_settings, screen, stats, sb, ship, aliens, enemy_bullets):
	enemy_bullets.update()
	for enemy_bullet in enemy_bullets.copy():
		if enemy_bullet.rect.top >= ai_settings.screen_height:
			enemy_bullets.remove(enemy_bullet)

"""创建外星人群 """   
def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings,screen) 
    # 调用函数：计算一行可容纳多少外星人
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建多行/多个外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 调用创建一个外星人函数：添加到外星人群
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

# 计算每行可容纳多少个外星人
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (ai_settings.alien_density_factor_x * alien_width))
    return number_aliens_x 

# 计算可以容纳多少行外星人
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - 
                            (6 * alien_height) - ship_height)
    number_rows = int(available_space_y / (ai_settings.alien_density_factor_y * alien_height))
    return number_rows

# 创建一个外星人（不是外星人群的成员）+放在当前行    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    # 计算外星人在当前行的位置
    alien_width = alien.rect.width # 外星人间距=外星人宽度（避免反复访问属性rect）
    alien.x = alien_width + ai_settings.alien_density_factor_x * alien_width * alien_number # 横坐标
    alien.rect.x = alien.x 
        #这里很重要！
        # 如果写作：alien.rect.x = alien_width + 2 * alien_width * alien_number
        # 屏幕只会出现一列外星人
    alien.rect.y = alien.rect.height + ai_settings.alien_density_factor_y * alien.rect.height * row_number +40 # 纵坐标
    aliens.add(alien) # 外星人群

# 1）碰到边缘
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

# 处理：下移+改方向标志
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

# 2）碰到底部
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets,enemy_bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # （处理：和撞飞船相同）
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets,enemy_bullets)
            break

# 3）撞飞船（处理）
def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets,enemy_bullets):
    # 碰撞后数目-1
    if stats.ships_left > 0:
        stats.ships_left -= 1

        enemies = []
        for alien in aliens:
            enemies.append(alien.rect.y)

        # 更新记分牌
        sb.prep_ships()    
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        enemy_bullets.empty()
        # 创建一群新的外星人并重置飞船
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停游戏
        sleep(0.5) 
    else:
        stats.ships_left = -1
        sb.prep_ships()
        stats.game_active = False
        pygame.mouse.set_visible(True) 


# 状态更新：调整外星人群（转向/重置）
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, enemy_bullets):
    check_fleet_edges(ai_settings, aliens) # a.触边
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens): # b.撞飞船【事件】
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, enemy_bullets) 

    if pygame.sprite.spritecollideany(ship, enemy_bullets): 
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, enemy_bullets)

    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets,enemy_bullets) # c.触底