import math
import time
import pygame
from typing import Tuple

import graphics
import sudoku
import constants as const

from mouse_handler import MouseHandler
from keyboard_handler import KeyboardHandler
from cell_manager import CellManager

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

    clock_str = clock_temp[1] + ":" + clock_temp[2]

    if clock_temp[0] != "00":
        clock_str = clock_temp[0] + ":" + clock_str

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
            new_cell = sudoku.Cell(cell_value)

            new_cell.row_index    = i
            new_cell.column_index = j
            
            if cell_value != 0:
                new_cell.starting = True
                new_cell.fg_color = const.COLOR_BLACK

            test_grid[i].append(new_cell)

    UICoord = graphics.UICoordinates(SCREEN_WIDTH, SCREEN_HEIGHT, test_grid)

    InitialTime = math.floor(time.time())
    ClockStr = generate_clock_str(InitialTime)

    selected_cell = [-1, -1]

    Mouse_Handler = MouseHandler(test_grid, UICoord, selected_cell)
    Highlight_Cells = sudoku.HighlightCells(test_grid, selected_cell)

    Keyboard_Handler = KeyboardHandler(test_grid, selected_cell)

    Cell_Manager = CellManager(test_grid, selected_cell)

    GameBoard = graphics.DrawBoard(SudokuSurface, UICoord)
    GameBoard.draw_complete_frame(test_grid, ClockStr)

    while running:

        event = pygame.event.wait()

        # ----- Pygame events -----

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            Keyboard_Handler.try_all_keys(event.key)

        elif event.type == pygame.KEYUP:
            Keyboard_Handler.key_released(event.key)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            Mouse_Handler.try_all_regions(event.button, event.pos)

        # ----- User events -----

        elif event.type == const.ID_UPDATE_TIMER:
            GameBoard.draw_clock(generate_clock_str(InitialTime))

        elif event.type == const.ID_REDRAW_CELLS:
            GameBoard.draw_cells(test_grid)
        
        elif event.type == const.ID_FLIP_BUFFER:
            pygame.display.flip()

        elif event.type == const.ID_SELECTED_CELL:
            Highlight_Cells.all_cells()

        elif event.type == const.ID_CLICKED_BUTTON:
            pass

        elif event.type == const.ID_CLICKED_EMPTY_AREA:
            Highlight_Cells.all_cells()

        elif event.type == const.ID_EDIT_CELL:
            Cell_Manager.insert_number(event.number)

        elif event.type == const.ID_DELETE_CELL:
            Cell_Manager.delete_number()

        elif event.type == const.ID_MOVE_SEL_CELL:
            Cell_Manager.change_selected_cell(event.direction)

        elif event.type == const.ID_INSERTED_NUMBER:
            Highlight_Cells.all_cells(event.mark)


    pygame.quit()