import pygame
import constants as const
from sudoku import Cell

SCREEN_RES = (SCREEN_WIDTH, SCREEN_HEIGHT) = (720, 576)
SUDOKU_RECT = (SUDOKU_WIDTH, SUDOKU_HEIGHT) = (509, 509)
# DEFAULT GRID SIZE IN PIXELS = 509


def global_init():

    pygame.init()
    pygame.font.init()

    sudoku_surface = pygame.display.set_mode(SCREEN_RES)

    pygame.display.set_caption("Sudoku Player")
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.time.set_timer(const.ID_UPDATE_TIMER, 1000)

    return sudoku_surface


def generate_grid() -> list:

    new_grid = []

    for i in range(9):

        new_grid.append([])

        for j in range(9):

            #cell_value = const.DEMO_GAME[i][j]
            cell_value = const.DEMO_GAME_2[i][j]
            new_cell = Cell(cell_value)

            new_cell.row_index = i
            new_cell.column_index = j

            if cell_value != 0:
                new_cell.starting = True
                new_cell.fg_color = const.COLOR_BLACK

            new_grid[i].append(new_cell)

    return new_grid
