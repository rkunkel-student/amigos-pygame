import pygame as pg
from random import choice
from UI import UI
from Tile import Tile
from Player import Player
from utils.settings import SCREEN_HEIGHT, SCREEN_WIDTH, TILESIZE

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pg.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pg.sprite.Group()

        # track enemies to aid in overlapp prevention
        self.enemy_sprites = pg.sprite.Group()

        # sprite setup
        self.create_map()

        # user interface
        self.ui = UI()
        self.game_paused = False

        # player
        self.player = Player([self.visible_sprites], self.obstacle_sprites, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "graphics\\player.png")

    def create_map(self):
        layouts = {}
        graphics = {}
        #layouts = {
        #    "boundary": import_csv_layout(f"map{FILE_DELIMITER}map_FloorBlocks.csv"),
        #    "grass": import_csv_layout(f"map{FILE_DELIMITER}map_Grass.csv"),
        #    "object": import_csv_layout(f"map{FILE_DELIMITER}map_Objects.csv"),
        #    "entities": import_csv_layout(f"map{FILE_DELIMITER}map_Entities.csv"),
        #}
        #graphics = {
        #    "grass": import_folder(f"graphics{FILE_DELIMITER}grass"),
        #    "object": import_folder(f"graphics{FILE_DELIMITER}objects"),
        #}

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                        if style == "boundary":
                            Tile((x, y), [self.obstacle_sprites], "invisible")


    def update(self):
        self.player.update()
        # pass the player to draw sprites based on their position
        self.visible_sprites.custom_draw(self.player)

        


class YSortCameraGroup(pg.sprite.Group):
    """Sprites are sorted by their y-coord, basic layer system"""

    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pg.math.Vector2()

        # edge case - floor/background
        self.floor_surf = pg.image.load(f"graphics\\background.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # get camera offset based on player
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # draw the floor before the sprites
        floor_offset = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset)

        # apply that offset to objects using this custom draw
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)