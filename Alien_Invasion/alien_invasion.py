# coding=utf-8

"""
作者: Duke
文件名: alien_invasion.py
创建时间: 2019/06/27-16:15
"""

import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, 'Play')
    # 创建存储游戏统计信息的实例，并创建计分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船、一个子弹编组和外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)  # 检查输入

        if stats.game_active:
            ship.update()  # 更新飞船
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)  # 更新子弹
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)  # 更新外星人

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)  # 绘制新屏幕

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
