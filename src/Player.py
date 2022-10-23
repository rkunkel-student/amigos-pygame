import logging
from typing import Sequence 
import pygame as pg


lh = logging.getLogger(__name__)


class Player(pg.sprite.Sprite):
    
    def __init__(self, groups, obstacle_sprites, x, y, image_path):
        super().__init__(groups)
        self.obstacle_sprites = obstacle_sprites

        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (5, 5))
        self.rect = self.image.get_rect(center=(x, y))
        self.hitbox = self.rect.inflate(10, 10)

        self.props = {'name': 'player'}
        self.props["direction"] = pg.math.Vector2(0, 0)
        self.props["speed"] = 10


    def input(self):
        events = pg.key.get_pressed()

        # left/right
        if events[pg.K_LEFT]:
            self.props["direction"].x = -1
            self.props["status"] = "left"
        elif events[pg.K_RIGHT]:
            self.props["direction"].x = 1
            self.props["status"] = "right"
        else:  # reset to 0
            self.props["direction"].x = 0

        # up/down
        if events[pg.K_UP]:
            self.props["direction"].y = -1
            self.props["status"] = "up"
        elif events[pg.K_DOWN]:
            self.props["direction"].y = 1
            self.props["status"] = "down"
        else:  # reset to 0
            self.props["direction"].y = 0

    def update(self):
        self.input()
        self.move()
        print(1)


    def move(self):
        # normalize direction vector
        if self.props["direction"].magnitude() != 0:
            self.props["direction"] = self.props["direction"].normalize()

        # horizontal movement
        self.hitbox.x += self.props["direction"].x * self.props["speed"]
        self.collision("horizontal")

        # vertical movement
        self.hitbox.y += self.props["direction"].y * self.props["speed"]
        self.collision("vertical")

        # move our sprite to match hitbox updates
        self.rect.center = self.hitbox.center


    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.props["direction"].x > 0:  # moving right...
                        # snap right side of player to left side of obstacle
                        self.hitbox.right = sprite.hitbox.left
                    if self.props["direction"].x < 0:  # moving left...
                        # snap reverse for otherside
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.props["direction"].y < 0:  # moving up...
                        # snap top side of player to bottom side of obstacle
                        self.hitbox.top = sprite.hitbox.bottom
                    if self.props["direction"].y > 0:  # moving down...
                        # snap reverse for otherside
                        self.hitbox.bottom = sprite.hitbox.top
