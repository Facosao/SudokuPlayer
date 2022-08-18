import math
import time
import pygame
from typing import Tuple

import graphics
import sudoku
import constants as const

SCREEN_RES  = (SCREEN_WIDTH, SCREEN_HEIGHT) = (720, 576)
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
    pygame.time.set_timer(const.ID_UPDATE_TIMER, 1000)

    running = True

    test_grid = []

    for i in range(9):

        test_grid.append([])

        for j in range(9):

            cell_value = const.DEMO_GAME[i][j]
            new_cell = sudoku.Cell(cell_value, const.COLOR_BLACK,
                                   const.COLOR_WHITE)

            test_grid[i].append(new_cell)

    UICoord = graphics.UICoordinates(SCREEN_WIDTH, SCREEN_HEIGHT, test_grid)

    InitialTime = math.floor(time.time())
    ClockStr = generate_clock_str(InitialTime)

    GameBoard = graphics.DrawBoard(SudokuSurface, UICoord)
    GameBoard.draw_complete_frame(test_grid, ClockStr)

    while running:

        event = pygame.event.wait()

        # ----- Primary pygame events -----

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                SP_return = const.SP_QUIT
            elif event.key == pygame.K_a:
                pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            if (event.button == const.LEFT_MOUSE_BUTTON):
                # Keep type declared in function parameter
                mouse_pos: Tuple[int, int] = event.pos
                sudoku.check_click_pos(mouse_pos, test_grid, UICoord)

        # ----- User events -----

        elif event.type == const.ID_UPDATE_TIMER:
            GameBoard.draw_clock(generate_clock_str(InitialTime))

        elif event.type == const.ID_REDRAW_CELLS:
            GameBoard.draw_cells(test_grid)
        
        elif event.type == const.ID_FLIP_BUFFER:
            pygame.display.flip()

    pygame.quit()