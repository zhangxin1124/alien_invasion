import sys
import pygame
from bullet import Bullet
from alien import Alien


def create_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    # 创建一个外星人,并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width



def update_bullets(bullets):
    """更新子弹的位置,并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到限制,就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)  # 加入编组


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:  # 右键按压事件监测
        ship.moving_right = True  # 开启右移开关
    elif event.key == pygame.K_LEFT:  # 左键按压事件监测
        ship.moving_left = True  # 开启左移开关
    elif event.key == pygame.K_SPACE:  # 空格按压事件监测
        fire_bullet(ai_settings, screen, ship, bullets)  # 监测是否允许发射子弹,如果允许,就发射一颗子弹
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ai_settings, screen, ship, bullets):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """相应案件和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 关闭游戏的事件
            sys.exit()

        elif event.type == pygame.KEYDOWN:  # 按键按下事件
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:  # 按键松开事件
            check_keyup_events(event, ai_settings, screen, ship, bullets)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像,并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)  # 显示屏幕
    ship.blitme()  # 显示飞船
    aliens.draw(screen)  # 显示外星人群

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
