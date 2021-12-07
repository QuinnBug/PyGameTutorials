from GameClasses import Vector, Game
import pygame as pg


class GameObject(pg.sprite.Sprite):
    def __init__(self, x, y, scale, img_file):
        super().__init__()
        img = pg.image.load(img_file)
        self.image = pg.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.lifetime = 0.0
        self.delta_time = 0.0
        self.position = Vector(x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta_time):
        self.delta_time = delta_time
        self.lifetime += self.delta_time
        self.rect.center = (self.position.x, self.position.y)


class PhysicsObject(GameObject):
    def __init__(self, x, y, scale, img_file):
        super().__init__(x, y, scale, img_file)
        self.gravity = Vector(0, 0)
        self.speed = Vector(0, 0)
        self.velocity = Vector(0, 0)
        self.move_boundary = Vector(0, 0)

    def set_physics(self, gravity):
        self.gravity = gravity

    def update(self, delta_time):
        self.velocity.add(self.gravity)


class Player(PhysicsObject):
    def __init__(self, x, y, scale, img_file):
        super().__init__(x, y, scale, img_file)
        self.input = Vector(0, 0)

    def update(self, delta_time):
        super().update(delta_time)
        self.check_inputs()
        self.move()

    def check_inputs(self):
        readd_events = []
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    self.input.x += 1
                if event.key == pg.K_a:
                    self.input.x -= 1
                if event.key == pg.K_s:
                    self.input.y += 1
                if event.key == pg.K_w:
                    self.input.y -= 1

            elif event.type == pg.KEYUP:
                if event.key == pg.K_d:
                    self.input.x -= 1
                if event.key == pg.K_a:
                    self.input.x += 1
                if event.key == pg.K_s:
                    self.input.y -= 1
                if event.key == pg.K_w:
                    self.input.y += 1
            else:
                readd_events.append(event)

        for event in readd_events:
            pg.event.post(event)

    def move(self):
        x_speed = self.speed.x * self.delta_time
        y_speed = self.speed.y * self.delta_time
        self.velocity.x += self.input.x * x_speed
        self.velocity.y += self.input.y * y_speed

        self.velocity.lerp(Vector(0, 0), self.velocity.magnitude() * (0.1 * self.delta_time))

        if self.velocity.magnitude() <= 0.05 and self.input.magnitude() == 0:
            self.velocity = self.velocity.multiply(Vector(0, 0))

        target = Vector(self.position.x + self.velocity.x,
                        self.position.y + self.velocity.y)

        if target.x > self.move_boundary.x or target.x < 0:
            target.x = self.rect.center[0]
            self.velocity.x *= -0.75

        if target.y > self.move_boundary.y or target.y < 0:
            target.y = self.rect.center[1]
            self.velocity.y *= -0.75

        self.position = Vector(target.x, target.y)

    # def draw(self, screen):
    #     super().draw(screen)
