import pygame as pg

LOAD_START_SCENE = pg.event.Event(pg.USEREVENT, name="start scene")

class SplashScreens:
    def __init__(self):
        self.image = pg.image.load("graphics\\rk-splash.png")
        self.rect = self.image.get_rect()

        self.start_time = pg.time.get_ticks()
        self.show_timer = 1200

    def update(self):
        if pg.time.get_ticks() - self.start_time > self.show_timer:
            pg.event.post(LOAD_START_SCENE)


    def draw(self, screen):
        screen.blit(self.image, self.rect)