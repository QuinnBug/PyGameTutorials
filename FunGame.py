import random
import pygame as pg
from pygame.locals import *

vec = pg.math.Vector2
screen_width = 500
screen_height = 500
FPS = 60
FramePerSec = pg.time.Clock()


class Coin(pg.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.height = 10
        self.width = 10
        self.image = pg.Surface((self.width, self.height))
        self.image.fill((175, 175, 25))
        self.rect = self.image.get_rect(center=position)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.height = 30
        self.width = 30
        self.image = pg.Surface((self.width, self.height))
        self.image.fill((0, 0, 175))
        self.rect = self.image.get_rect(center=(10, 420))

        self.pos = vec((10, 385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.speed = 0.5
        self.friction = -0.12
        self.grav_mod = 1
        self.jumps = 2
        self.switches = 1

        self.score = 0

    def update(self, platforms, coins):
        self.move()
        self.collisions(platforms, coins)

    def collisions(self, platforms, coins):
        hits = pg.sprite.spritecollide(self, platforms, False)
        if hits:
            dist_top = hits[0].rect.top - self.rect.bottom
            dist_bot = hits[0].rect.bottom - self.rect.top

            if dist_top < 0:
                dist_top *= -1

            if dist_bot < 0:
                dist_bot *= -1

            if dist_top < dist_bot:
                self.pos.y = hits[0].rect.top + 1
            elif dist_top > dist_bot:
                self.pos.y = hits[0].rect.bottom + self.height
            else:
                if self.grav_mod > 0:
                    self.pos.y = hits[0].rect.top + 1
                elif self.grav_mod < 0:
                    self.pos.y = hits[0].rect.bottom + self.height

            self.vel.y = 0
            self.jumps = 2
            self.switches = 1

        hits = pg.sprite.spritecollide(self, coins, True)
        if hits:
            self.score += 1

    def move(self):
        self.acc = vec(0, 0.5 * self.grav_mod)

        pressed_keys = pg.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -self.speed
        if pressed_keys[K_RIGHT]:
            self.acc.x = self.speed

        self.acc.x += self.vel.x * self.friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > screen_width - (self.width/2):
            self.pos.x = screen_width - (self.width/2)
        if self.pos.x < self.width/2:
            self.pos.x = self.width/2

        if self.pos.y > screen_height:
            self.pos.y = screen_height / 2
        if self.pos.y < 0:
            self.pos.y = screen_height / 2

        self.rect.midbottom = self.pos

    def jump(self):
        if self.jumps > 0:
            self.vel.y = -10 * self.grav_mod
            self.jumps -= 1

    def grav_switch(self):
        if self.switches > 0:
            self.grav_mod *= -1
            self.switches -= 1


class Platform(pg.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pg.Surface(size)
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(center=position)


class Game:
    def __init__(self):
        pg.init()
        pg.font.init()

        self.font = pg.font.SysFont('Comic Sans MS', 18)

        self.d_surface = pg.display.set_mode((screen_width, screen_height))
        self.screen = pg.display.set_mode([500, 500])
        self.running = True
        self.player = Player()
        self.platform_list = [Platform(size=(screen_width, 20), position=(screen_width / 2, screen_height - 25)),
                              Platform(size=(screen_width, 20), position=(screen_width / 2, 25))]
        self.platform_group = pg.sprite.Group()
        self.coin_group = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()

        self.all_sprites.add(self.player)

        for p in self.platform_list:
            self.all_sprites.add(p)
            self.platform_group.add(p)

        self.new_coins()

    def new_platforms(self):
        for p in self.platform_group:
            if self.all_sprites.has(p):
                self.all_sprites.remove(p)

        self.platform_group.empty()

        for p in self.platform_list:
            self.all_sprites.add(p)
            self.platform_group.add(p)

        for x in range(random.randint(1, 3)):
            p = Platform(size=(screen_width/3, 10),
                                position=(random.randint(0, screen_width), screen_height/5 * (x+1)))
            self.all_sprites.add(p)
            self.platform_group.add(p)

    def new_coins(self):
        for x in range(random.randint(3, 6)):
            coin = Coin((random.randint(0, screen_width - 10), random.randint(75, screen_height - 75)))
            hits = pg.sprite.spritecollide(coin, self.platform_group, False)
            if hits:
                if coin.rect.center[1] > screen_height/2:
                    coin.rect.move(0, -15)
                else:
                    coin.rect.move(0, 15)
            self.all_sprites.add(coin)
            self.coin_group.add(coin)

    def update(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.player.jump()
                    if event.key == pg.K_UP:
                        self.player.grav_switch()

            self.d_surface.fill((125, 125, 125))

            for s in self.all_sprites:
                self.d_surface.blit(s.image, s.rect)

            self.player.update(self.platform_group, self.coin_group)

            if not self.coin_group.__len__() > 0:
                self.new_platforms()
                self.new_coins()

            score_surf = self.font.render("SCORE: " + str(self.player.score), False, (200, 200, 200))
            self.d_surface.blit(score_surf, (0, 12))
            pg.display.update()
            FramePerSec.tick(FPS)


game = Game()

game.update()
