# -*- coding: utf-8 -*-
"""Tile support for tilemap."""

import pygame
from utils.settings import TILESIZE

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        y_offset = 10
        self.image = surface

        if sprite_type == "object":
            # images are 64x64, 64x128, or 128x128
            # by subtracting the TILESIZE (64) we move the image up
            # and the tilemap csv representation aligns with what we expect
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft=pos)

        # base hitbox off image to allow some overlap
        self.hitbox = self.rect.inflate(0, y_offset)
