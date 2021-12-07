from GameClasses import Vector, Game
from GameObjects import GameObject, Player, PhysicsObject
import pygame as pg

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)




game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
game.add_go(GameObject(game.center.x, game.center.y, 1, "img/circle.png"))
game.add_go(Player(game.center.x, game.center.y, 0.2, "img/player.png"))
while game.run:
    game.update()
pg.quit()
