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
COLOR_USER_CELL       = (  0, 114, 227)

# Number colors
COLOR_STARTING_NUMBER = (  0,   0,   0)
COLOR_USER_NUMBER     = (  0,   0, 255) # Change to correct color
COLOR_INVALID_NUMBER  = (255,   0,   0) # Change to correct color

# Border sizes (outer border and cell border)
CELL_BORDER  = 1
OUTER_BORDER = 2

# Controls
LEFT_MOUSE_BUTTON = 1

# Pygame user event ID
ID_UPDATE_TIMER       = pygame.USEREVENT + 2
ID_REDRAW_CELLS       = pygame.USEREVENT + 3
ID_FLIP_BUFFER        = pygame.USEREVENT + 4
ID_CLICKED_CELL       = pygame.USEREVENT + 5
ID_CLICKED_BUTTON     = pygame.USEREVENT + 6
ID_CLICKED_EMPTY_AREA = pygame.USEREVENT + 7

# Pygame user event object
EVENT_UPDATE_TIMER       = pygame.event.Event(ID_UPDATE_TIMER)
EVENT_REDRAW_CELLS       = pygame.event.Event(ID_REDRAW_CELLS)
EVENT_FLIP_BUFFER        = pygame.event.Event(ID_FLIP_BUFFER)
EVENT_CLICKED_CELL       = pygame.event.Event(ID_CLICKED_CELL)
EVENT_CLICKED_BUTTON     = pygame.event.Event(ID_CLICKED_BUTTON)
EVENT_CLICKED_EMPTY_AREA = pygame.event.Event(ID_CLICKED_EMPTY_AREA)

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
