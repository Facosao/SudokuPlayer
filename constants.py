import pygame

# General colors
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (  0,   0,   0)

# Border colors
COLOR_GRID_DIVIDER    = ( 52,  72,  97)
COLOR_GRID_BACKGROUND = (203, 208, 219)

# Cell colors
COLOR_SELECTED_CELL   = (187, 222, 251)
COLOR_SAME_NUMBER     = (195, 215, 234)
COLOR_RULE_HIGHLIGHT  = (226, 235, 246)

# Number colors
COLOR_STARTING_NUMBER = (  0,   0,   0)
COLOR_USER_NUMBER     = (  0,   0, 255) # Change to correct color
COLOR_INVALID_NUMBER  = (255,   0,   0) # Change to correct color

# Border sizes (outer border and cell border)
CELL_BORDER  = 1
OUTER_BORDER = 2

# Controls
LEFT_MOUSE_BUTTON = 1

# Pygame user event
PYGAME_UPDATE_TIMER = pygame.USEREVENT + 10

# Event return codes
SP_CONTINUE     = 0
SP_REDRAW_CELLS = 1
SP_FLIP_BUFFER  = 2
SP_QUIT         = 3

# Demo game (Testing only)
DEMO_GAME = [[0, 0, 6, 2, 0, 0, 0, 0, 5],
             [0, 0, 0, 4, 0, 0, 3, 0, 0],
             [2, 0, 0, 0, 0, 3, 0, 1, 6],
             [0, 2, 0, 3, 0, 0, 0, 0, 0],
             [7, 0, 3, 0, 0, 0, 0, 4, 9],
             [0, 1, 0, 9, 0, 2, 7, 0, 8],
             [0, 3, 0, 6, 4, 0, 0, 0, 0],
             [0, 0, 2, 5, 0, 0, 0, 9, 0],
             [5, 0, 9, 0, 0, 0, 1, 0, 0]]
