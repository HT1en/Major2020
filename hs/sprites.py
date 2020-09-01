# Sprite classes for platform game
import pygame as pg
import os
from settings import *
vec = pg.math.Vector2

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


class enemy(pg.sprite.Sprite):
    def __init__(self, game, plat):
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load(os.path.join(img_folder,"enemy.png")).convert()
        self.game = game
        self.rect = self.image.get_rect

    def enemeymovement(enemy, x, y):
        direction = random.randint(1 ,8)
        if direction == 1:
            y += 1
        if direction == 2:
            x += 1
            y += 1
        if direction == 3:
            x += 1
        if direction == 4:
            x += 1
            y -= 1
        if direction == 5:
            y -= 1
        if direction == 6:
            x -= 1
            y -= 1
        if direction == 7:
            x -= 1
        if direction == 8:
            x -= 1


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
            self.game.jump_sound.play()
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            camera_dx = 3
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            camera_dx = -3

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        hits = pg.sprite.spritecollide(self,self.game.platforms, False)
        if hits:
            self.acc.y = 1
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
        self.image = pg.image.load(os.path.join(img_folder,"pix.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
