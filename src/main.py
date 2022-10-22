# -*- coding: utf-8 -*-
#! /usr/bin/python3
# (C) RKADE GAMES, LLC. Freedom to distribute.
"""PyGame Halloween Contest 2022-10"""

import logging
from sys import stdout, exit
import pygame as pg
from utils.settings import SCREEN_SIZE, FPS
from screens.SplashScreens import SplashScreens

# ---------------------------------------- LOGGING ---------------------------------------- # 

fh = logging.FileHandler("debug.log", mode="w")
ch = logging.StreamHandler(stdout)

ch.setLevel(logging.ERROR)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S %p",
    level=logging.DEBUG,
    handlers=[fh, ch]
)

lh = logging.getLogger(__name__)
lh.debug("Logger created..")

# ---------------------------------------- END LOGGING ---------------------------------------- # 
# ---------------------------------------- PyGame Init ---------------------------------------- #

pg.mixer.pre_init
pg.init()

# ---------------------------------------- END PyGame Init ---------------------------------------- #


class StartMenu:
    def __init__(self):
        self.font = pg.font.Font(pg.font.get_default_font(), 32)
        self.title_surface = self.font.render("Start Scene", True, "white")

    def update(self):
        pass

    def draw(self, screen: pg.surface.Surface):
        rect = screen.get_rect()
        offset = pg.math.Vector2(0, 50)
        title_rect = self.title_surface.get_rect(midtop=rect.midtop + offset)
        screen.blit(self.title_surface, title_rect)


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()

        pg.display.set_caption("")  # Window Title
        pg.display.set_icon(pg.image.load("graphics\\logo.png"))

        self.level = SplashScreens()


    def handle_user_events(self, event):
        if event.name == "start scene":
            self.level = StartMenu()


    def handle_keydown_events(self, event):
        lh.info(event)



    def handle_keyup_events(self, event):
        lh.info(event)
  

    def run(self):
        while True:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

                # handle events 
                elif event.type == pg.USEREVENT:
                    self.handle_user_events(event)

                elif event.type == pg.KEYDOWN:
                    self.handle_keydown_events(event)

                elif event.type == pg.KEYUP:
                    self.handle_keyup_events(event)

                # elif event.type == pg.MOUSEBUTTONDOWN:
                #     pass
                # elif event.type == pg.MOUSEBUTTONUP:
                #     pass
                # elif event.type == pg.MOUSEMOTION:
                #     pass
                # elif event.type == pg.MOUSEWHEEL:
                #     pass


            # wipe the screen before drawing
            self.screen.fill('black')

            # draw 
            self.level.draw(self.screen)

            # update 
            self.level.update()
            pg.display.update()
            self.clock.tick(FPS)
            

def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main() 
