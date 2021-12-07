from GameClasses import Vector, Game
from GameObjects import GameObject, Player, PhysicsObject
import pygame as pg

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

player = Player(game.center.x, game.center.y, 0.2, "img/player.png")
player.set_player_stats(game.screen_size, Vector(10, 2), Vector(0, 1), 0.1)
game.add_go(player)

game.add_go(GameObject(game.center.x, game.center.y, 1, "img/circle.png"))

ball = PhysicsObject(game.center.x, game.center.y, 0.5, "img/circle.png")
ball.set_physics(game.screen_size, Vector(0.5, -1), 0)
game.add_go(ball)


while game.run:
    game.update()
pg.quit()
