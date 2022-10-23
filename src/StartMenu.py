import pygame as pg
from utils.settings import SCREEN_HEIGHT, SCREEN_WIDTH

LOAD_LEVEL_SCENE = pg.event.Event(pg.USEREVENT, name="level 1")

class StartMenu:
    def __init__(self):
        self.font = pg.font.Font(pg.font.get_default_font(), 32)
        self.title_surface = self.font.render("Start Scene", True, "white")
        self.play_surface = self.font.render("Play", True, "red")
        self.hovered = False

    def update(self):
        self.draw()
        
        event_pos = pg.mouse.get_pos()
        event_click = pg.mouse.get_pressed()

        box_rect = pg.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 40, 200, 80)
        if box_rect.collidepoint(event_pos):
            self.hovered = True
        else:
            self.hovered = False

        if event_click[0] and self.hovered:
            pg.event.post(LOAD_LEVEL_SCENE)

    def draw(self):
        screen = pg.display.get_surface()
        rect = screen.get_rect()
        offset = pg.math.Vector2(0, 50)
        title_rect = self.title_surface.get_rect(midtop=rect.midtop + offset)
        screen.blit(self.title_surface, title_rect)

        text_rect = pg.Rect(SCREEN_WIDTH/2 - 32, SCREEN_HEIGHT/2 - 16, 200, 80)
        box_rect = pg.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 40, 200, 80)

        if not self.hovered:
            pg.draw.rect(screen, 'white', box_rect)
        else:
            pg.draw.rect(screen, 'grey', box_rect)

        pg.draw.rect(screen, 'red', box_rect, 4)
        screen.blit(self.play_surface, text_rect)