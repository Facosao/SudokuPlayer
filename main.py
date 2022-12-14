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

SCREEN_RES = (SCREEN_WIDTH, SCREEN_HEIGHT) = (800, 600)
SUDOKU_RECT = (SUDOKU_WIDTH, SUDOKU_HEIGHT) = (509, 509)
# DEFAULT GRID SIZE IN PIXELS = 509


if __name__ == "__main__":

    #  Instantiating objects

    SudokuSurface = init.global_init()

    test_grid = init.generate_grid()
    UICoord = graphics.UICoordinates(test_grid)

    clock_obj = Clock()
    selected_cell = [-1, -1]

    Mouse_Handler = MouseHandler(test_grid, UICoord, selected_cell)
    Highlight_Cells = sudoku.HighlightCells(test_grid, selected_cell)

    Keyboard_Handler = KeyboardHandler(test_grid, selected_cell)
    Cell_Manager = CellManager(test_grid, selected_cell)
    global_undo = Undo(test_grid, selected_cell)
    obj_draw_ui = graphics.DrawUI(UICoord)

    GameBoard = graphics.DrawBoard(UICoord)
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

        elif event.type == pygame.VIDEORESIZE:
            SudokuSurface = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            UICoord = graphics.UICoordinates(test_grid)
            Mouse_Handler = MouseHandler(test_grid, UICoord, selected_cell)
            obj_draw_ui = graphics.DrawUI(UICoord)
            GameBoard = graphics.DrawBoard(UICoord)
            GameBoard.draw_complete_frame(test_grid, clock_obj.generate_clock_str())

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
            global_undo.push(event.old_cell)

        elif event.type == const.ID_UNDO_POP:
            global_undo.pop()

        elif event.type == const.ID_DRAW_TOGGLE:
            obj_draw_ui.draw_toggle(event.is_active)

    pygame.quit()
