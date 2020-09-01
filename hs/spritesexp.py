# Sprite classes for platform game
import pygame as pg
import os
from settings import *
vec = pg.math.Vector2

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class spritesheet:
    def __init__(self,filename,cols,rows):
        self.sheet = pg.image.load(filename)

        self.cols= cols
        self.rows= rows
        self.totalCellCount = cols * rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width / cols
        h = self.cellHeight = self.rect.height / rows
        hw,hh = self.cellCenter = (w/2,h/2)
        self.HW = hw
        self.HH = hh

        self.cells = list([(index%cols*w,index/cols*h) for index in range(self.totalCellCount)])
        self.handle = list([
            (0,0),(-hw,0),(-w,0),
            (0,-hh),(-hw,-hh),(-w,-hh),
            (0,-h),(-hw,-h),(-w,h),])

    def draw(self,surface,cellIndex,x,y,handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]))

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder,"cool.png")).convert()
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self,self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -10

    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        hits = pg.sprite.spritecollide(self,self.game.platforms, False)
        if hits:
            self.acc = 0
        self.vel += self.acc
        self.pos += self.vel + self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
