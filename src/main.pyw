# -*- coding: utf-8 -*-
#! /usr/bin/python3
# (C) RKADE GAMES, LLC. Freedom to distribute.
"""PyGame Halloween Contest 2022-10-22"""

import logging
from sys import stdout, exit
import pygame as pg
from utils.settings import SCREEN_SIZE, FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from SplashScreens import SplashScreens
from StartMenu import StartMenu
from Level import Level

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
        elif event.name == "level 1":
            self.level = Level()

    def run(self):
        while True:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

                # handle events 
                elif event.type == pg.USEREVENT:
                    self.handle_user_events(event)

            # wipe the screen before drawing
            self.screen.fill('black')

            # update 
            self.level.update()
            pg.display.update()
            self.clock.tick(FPS)
            

def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main() 
