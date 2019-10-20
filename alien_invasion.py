import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船,一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens)

    # 开始游戏的主循环
    while True:

        # 监控事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()  # 更新飞船的位置

        # 更新子弹的位置,删除消失的子弹
        gf.update_bullets(bullets)

        # 每次循环时都会重绘屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # 让最近绘制的屏幕课件
        pygame.display.flip()


run_game()



