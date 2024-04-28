import pygame as pg
pg.init
xmax = 100
ymax = 1000

resolution = (xmax, ymax)
screen = pg.display.set_mode(resolution)

rect = screen.get_rec()


pg.quit