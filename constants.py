import pygame

# General colors
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (  0,   0,   0)

# Border colors
COLOR_GRID_DIVIDER    = ( 52,  72,  97)
COLOR_GRID_BACKGROUND = (203, 208, 219)

# Cell colors
COLOR_SELECTED_CELL     = (187, 222, 251)
COLOR_SAME_NUMBER       = (195, 215, 234)
COLOR_RULE_HIGHLIGHT    = (226, 235, 246)
COLOR_INVALID_NUMBER_BG = (247, 207, 214)

# Number colors
COLOR_USER_NUMBER       = (  0, 114, 227)
COLOR_INVALID_NUMBER_FG = (229,  92, 108)
COLOR_PENCIL_MARK       = (110, 124, 140)

# Border sizes (outer border and cell border)
CELL_BORDER  = 1
OUTER_BORDER = 2

# Controls
LEFT_MOUSE_BUTTON = 1

# Pygame user event ID
ID_UPDATE_TIMER       = pygame.USEREVENT + 2
ID_REDRAW_CELLS       = pygame.USEREVENT + 3
ID_FLIP_BUFFER        = pygame.USEREVENT + 4
ID_SELECTED_CELL      = pygame.USEREVENT + 5
ID_CLICKED_BUTTON     = pygame.USEREVENT + 6
ID_CLICKED_EMPTY_AREA = pygame.USEREVENT + 7
ID_DELETE_CELL        = pygame.USEREVENT + 8
ID_EDIT_CELL          = pygame.USEREVENT + 9
ID_MOVE_SEL_CELL      = pygame.USEREVENT + 10
ID_INSERTED_NUMBER    = pygame.USEREVENT + 11

# Pygame user event object
EVENT_UPDATE_TIMER        = pygame.event.Event(ID_UPDATE_TIMER)
EVENT_REDRAW_CELLS        = pygame.event.Event(ID_REDRAW_CELLS)
EVENT_FLIP_BUFFER         = pygame.event.Event(ID_FLIP_BUFFER)
EVENT_SELECTED_CELL       = pygame.event.Event(ID_SELECTED_CELL)
EVENT_CLICKED_BUTTON      = pygame.event.Event(ID_CLICKED_BUTTON)
EVENT_CLICKED_EMPTY_AREA  = pygame.event.Event(ID_CLICKED_EMPTY_AREA)
EVENT_DELETE_CELL         = pygame.event.Event(ID_DELETE_CELL)
#EVENT_EDIT_CELL         -> Created from KeyboardHandler
#EVENT_MOVE_SEL_CELL     -> Created from KeyboardHandler
#EVENT_INSERTED_NUMBER   -> Created from CellManager

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
