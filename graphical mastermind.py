import pygame as pg
pg.init
xmax = 100
ymax = 1000

resolution = (xmax, ymax)
screen = pg.display.set_mode(resolution)
#todo:
# convert random numbers to colours
# place the code under a black box at the top of the screen with an option to (show/hide)
# as the user types the digits, place them in the rows
# using white and red give oopcorrect and correct
# add a button to quit
# one to restart
# one to change settigns

black = (0, 0, 0)
scrrect = screen.get_rect()
pg.draw.rect(screen, black, scrrect)

pg.quit