import pygame

import graphics
import sudoku
import constants as const
import init

from mouse_handler import MouseHandler
from keyboard_handler import KeyboardHandler
from cell_manager import CellManager
from clock import Clock
from undo import Undo

SCREEN_RES = (SCREEN_WIDTH, SCREEN_HEIGHT) = (720, 576)
SUDOKU_RECT = (SUDOKU_WIDTH, SUDOKU_HEIGHT) = (509, 509)
# DEFAULT GRID SIZE IN PIXELS = 509


if __name__ == "__main__":

    #  Instantiating objects

    SudokuSurface = init.global_init()

    test_grid = init.generate_grid()
    UICoord = graphics.UICoordinates(SCREEN_WIDTH, SCREEN_HEIGHT, test_grid)

    clock_obj = Clock()
    selected_cell = [-1, -1]

    Mouse_Handler = MouseHandler(test_grid, UICoord, selected_cell)
    Highlight_Cells = sudoku.HighlightCells(test_grid, selected_cell)

    Keyboard_Handler = KeyboardHandler(test_grid, selected_cell)
    Cell_Manager = CellManager(test_grid, selected_cell)
    global_undo = Undo(test_grid, selected_cell)

    GameBoard = graphics.DrawBoard(SudokuSurface, UICoord)
    GameBoard.draw_complete_frame(test_grid, clock_obj.generate_clock_str())

    running = True

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
            GameBoard.draw_clock(clock_obj.generate_clock_str())

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

        elif event.type == const.ID_UNDO_PUSH:
            #print("event cell =", event.old_cell.value)
            global_undo.push(event.old_cell)

        elif event.type == const.ID_UNDO_POP:
            global_undo.pop()
            #print("sel_cell = [%d, %d]" % (selected_cell[0], selected_cell[1]))

    pygame.quit()
