import pygame
import random


from ..tools import button 
from ..tools import text

def menu(window:pygame.Surface):
    
    window_width =  1280
    window_height = 720
    
    r=random.randrange(100,255)
    g=random.randrange(100,255)
    b=random.randrange(100,255)
    menu_title=text((window_width//2,window_height//8),'2048',(r,g,b),window_width//10,'game\\ui\\src\\font\\Milky Mania.ttf')
    start=button((window_width//2,window_height*5//16),'start',150,font='Microsoft YaHei')
    multiplayer=button((window_width//2,window_height*7//16),'multiplayer',150)
    setting=button((window_width//2,window_height*9//16),'Settings',150)
    
    menu_title.show(window)
    start.show(window)
    multiplayer.show(window)
    setting.show(window)
    
    pygame.display.flip()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                if start.onclick(mouse_pos):
                    print('start')
                    pass #运行单人游戏界面
                elif multiplayer.onclick(mouse_pos):
                    print('multi')
                    pass #运行多人游戏界面
                elif setting.onclick(mouse_pos):
                    print('setting')
                    pass #运行设置界面


def main():
    window_width =  1280
    window_height = 720
    
    window=pygame.display.set_mode((window_width,window_height))
    pygame.init()
    # pygame.time.set_timer(pygame.USEREVENT, 5000)
    while(True):
        menu(window)
        window.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()