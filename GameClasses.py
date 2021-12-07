import math
import pygame as pg
import pygame.display


class Game:
    def __init__(self, width, height):
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption('QGame')
        self.run = True
        self.game_objs = []
        self.screen_size = Vector(width, height)
        self.center = Vector(width/2, height/2)
        self.FPS = 999
        self.clock = pg.time.Clock()

    def update(self):
        self.draw_objs()
        self.event_update()
        self.objs_update()
        self.clock.tick(self.FPS)

    def draw_objs(self):
        self.screen.fill((0, 0, 0))
        for obj in self.game_objs:
            obj.draw(self.screen)
            # self.screen.blit(obj.image, obj.rect)
        pygame.display.flip()

    def event_update(self):
        if pg.event.peek(pg.QUIT):
            return False
        return True

    def objs_update(self):
        delta_time = self.clock.get_time() / 1000

        for obj in self.game_objs:
            obj.update(delta_time)

    def add_go(self, obj):
        self.game_objs.append(obj)

    def delete_go(self, obj):
        self.game_objs.remove(obj)
        del obj


class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def minus(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)

    def multiply(self, other):
        return Vector(self.x * other.x,
                      self.y * other.y,
                      self.z * other.z)

    def lerp(self, target, rate):
        if target.x > self.x:
            self.x += rate
        elif target.x < self.x:
            self.x -= rate

        if target.y > self.y:
            self.y += rate
        elif target.y < self.y:
            self.y -= rate

        if self.y - rate < target.y < self.y + rate:
            self.y = target.y

        if self.x - rate < target.x < self.x + rate:
            self.x = target.x

    def magnitude(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))
