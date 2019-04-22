import pygame                   # 导入pygame库
from pygame.locals import *     # 导入pygame库中的一些常量
from sys import exit            # 导入sys库中的exit函数
import os


#定义窗口的分辨率
SCREEN_WIDTH =  500
SCREEN_HEIGHT = 500

# 计数ticks == new add ==
ticks = 0
# 计数ticks == new add ==
  
# 初始化游戏
pygame.init()                   # 初始化pygame
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])     # 初始化窗口
pygame.display.set_caption('fly')       # 设置窗口标题
 
# 载入背景图
background = pygame.image.load('/Users/xccai/Downloads/background.png').convert()
#载入资源图片 == new add ==
shoot_img = pygame.image.load('/Users/xccai/Downloads/shoot.png').convert()

# 用subsurface剪切读入的图片
hero1_rect = pygame.Rect(0, 0, 146, 169)
hero2_rect = pygame.Rect(0, 0, 146, 169)
hero1 = shoot_img.subsurface(hero1_rect)
hero2 = shoot_img.subsurface(hero2_rect)
hero_pos = [200, 200]
# 载入资源图片 == new add ==
 
# 事件循环(main loop)
while True:
 
    # 绘制背景
    screen.blit(background, (0, 0))
     
    # 绘制飞机 == new add ==
    if ticks % 50 < 25:
        screen.blit(hero1, hero_pos)
    else:
        screen.blit(hero2, hero_pos)
    ticks += 1
    # 绘制飞机  == new add ==
     
    # 更新屏幕
    pygame.display.update()                                         
     
    # 处理游戏退出
    # 从消息队列中循环取
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
