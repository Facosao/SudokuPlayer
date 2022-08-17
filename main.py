import math
from random import random
import time
from typing import Tuple
import pygame

import graphics
import sudoku
import constants as const

SCREEN_RES = (SCREEN_WIDTH, SCREEN_HEIGHT) = (720, 576)
SUDOKU_RECT = (SUDOKU_WIDTH, SUDOKU_HEIGHT) = (509, 509)

# DEFAULT GRID SIZE IN PIXELS = 509


def generate_clock_str(initial_time: int) -> str:

    current_time = math.floor(time.time())
    current_time -= initial_time

    clock_temp = []

    clock_temp.append(current_time // 3600)
    clock_temp.append(current_time // 60)
    clock_temp.append(current_time % 60)
    
    for i in range(3):
        
        if (clock_temp[i] < 10):
            clock_temp[i] = "0" + str(clock_temp[i])
        else:
            clock_temp[i] = str(clock_temp[i])

    clock_str = clock_temp[0] + ":" + clock_temp[1] + ":" + clock_temp[2]

    return clock_str


if __name__ == "__main__":

    pygame.init()
    pygame.font.init()

    SudokuSurface = pygame.display.set_mode(SCREEN_RES)

    pygame.display.set_caption("Sudoku Player")
    pygame.event.set_blocked(pygame.MOUSEMOTION)

    UPDATE_TIMER = 10
    pygame.time.set_timer(pygame.USEREVENT + UPDATE_TIMER, 1000)

    running: bool = True

    test_grid = []

    for i in range(9):

        test_grid.append([])

        for j in range(9):

            cell_value = 0
            if (random() > 0.5):
                cell_value = math.floor(random() * 10)

            new_cell = sudoku.Cell(cell_value, const.COLOR_BLACK,
                                   const.COLOR_WHITE)

            test_grid[i].append(new_cell)

    positions = graphics.ObjectPosition(SCREEN_WIDTH, SCREEN_HEIGHT, test_grid)

    initial_time = math.floor(time.time())
    clock_str = generate_clock_str(initial_time)

    graphics.draw_complete_frame(SudokuSurface, clock_str, positions,
                                 test_grid)

    initial_time = math.floor(time.time())

    while running:

        event = pygame.event.wait()
        return_code = const.NO_ACTION

        # TODO: Revert to match case with const.UPDATE_TIMER
        if event.type == pygame.QUIT:
            running = False

        elif event.type == (pygame.USEREVENT + UPDATE_TIMER):

            clock_str = generate_clock_str(initial_time)
            graphics.draw_clock(SudokuSurface, clock_str)

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                running = False
            elif event.key == pygame.K_a:
                pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button: int = event.button

            if (mouse_button == const.LEFT_MOUSE_BUTTON):

                mouse_pos: Tuple[int, int] = event.pos
                return_code = sudoku.check_click_pos(mouse_pos, test_grid,
                                                     positions)

        # ----- Process event return code -----

        if return_code == const.NO_ACTION:
            continue

        elif return_code == const.REDRAW_CELLS:
            graphics.draw_cells(SudokuSurface, positions, test_grid)

    pygame.quit()