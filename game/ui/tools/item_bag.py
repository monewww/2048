import pygame
import numpy as np
from ..tools.common import load_image
from .common import abstract_onclick_comp

class item_bag(abstract_onclick_comp):
    ## 传入start_pos是因为item_bag返回的是局部的surface而不是在整个window上画，此时在onclick时需要知道是否点击在范围中了
    def __init__(self,size,item_bag=np.zeros(12,int),start_pos=(0,0)):
        self.start_pos=start_pos
        self.width=size[0]
        self.height=size[1]
        self.item_bag=item_bag
        self.item_to_png={
            1:'game\\ui\\assets\\images\\random.png',
            2:'game\\ui\\assets\\images\\copy_32.png',
            3:'game\\ui\\assets\\images\\copy_128.png',
            4:'game\\ui\\assets\\images\\frozen_time.png',
            5:'game\\ui\\assets\\images\\bigger_num.png',
            6:'game\\ui\\assets\\images\\bigger_num.png',#我不到啊
            7:'game\\ui\\assets\\images\\bigger_num.png',#我不到啊
            8:'game\\ui\\assets\\images\\double.png',
            9:'game\\ui\\assets\\images\\smaller_num.png',
            10:'game\\ui\\assets\\images\\merge_update.png',
            11:'game\\ui\\assets\\images\\remove.png',
            12:'game\\ui\\assets\\images\\remove.png',#我还是不到啊
        }
        self.window=pygame.Surface((self.width,self.height)).convert_alpha()
        self.window.fill((0,0,0,0))
        self.update(self.item_bag)
        self.last_onclick=-1
        
    def get_text(self):
        return self.last_onclick
        
    def update(self,item_bag):
        self.item_bag=item_bag
        item_pos=0
        png_width=self.width//4
        png_height=self.height//3
        self.window.fill((0,0,0,0))
        for item in item_bag:
            if item in self.item_to_png.keys():
                item_png=load_image(self.item_to_png[item],(png_width,png_height))# 分为4*3共12个道具
                self.window.blit(item_png,(png_width*(item_pos%4),png_height*(item_pos//4)))
                item_pos+=1
    #如果不在范围中返回false,否则返回对应的道具编号或-1
    def onclick(self,mouse_pos):
        mouse_pos=(
            mouse_pos[0]-self.start_pos[0],
            mouse_pos[1]-self.start_pos[1]
        )
        if 0<mouse_pos[0]<self.width and 0<mouse_pos[1]<self.height:
            item_num=(mouse_pos[0]*4//self.width)+4*(mouse_pos[1]*3//self.height)
            self.last_onclick=self.item_bag[item_num] if self.item_bag[item_num]!=0 else False
            return self.last_onclick
        else:
            return False
        
        
    def get_surface(self):
        return self.window        