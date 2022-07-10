from cmath import rect
import sys
import pygame


""" 
screen = pygame.display.set_mode((1200, 800))
screen.fill((230, 230, 230))
pygame.display.set_caption("窗口测试")
screen_rect=screen.get_rect()


image = pygame.image.load('alien\images\ship.jpg')
# 获取图片的rect参数
rect = image.get_rect()
# 把图片位置标注为屏幕中间
rect.midbottom=screen_rect.midbottom

# 把图片放到屏幕上
screen.blit(image, rect)
# 让绘制屏幕可见，不然打开是个黑窗口
pygame.display.flip()

# 让屏幕等待获取事件，不然窗口会一闪而过
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 """