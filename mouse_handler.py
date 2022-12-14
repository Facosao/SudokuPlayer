from typing import Tuple
import constants as const
import graphics
import pygame


class MouseHandler:

    def __init__(self, grid, ui_coord, selected_cell) -> None:
        self.grid: list = grid
        self.coord: graphics.UICoordinates = ui_coord
        self.selected_cell: list = selected_cell

    def try_all_regions(self, mouse_button: int, mouse_pos: Tuple) -> None:

        if mouse_button != const.LEFT_MOUSE_BUTTON:
            return

        # ----------------------------------
        if self.__try_cell_click(mouse_pos):
            return pygame.event.post(const.EVENT_SELECTED_CELL)

        # ----------------------------------
        if self.__try_button_click():
            return pygame.event.post(const.EVENT_CLICKED_BUTTON)

        # ----------------------------------
        return pygame.event.post(const.EVENT_CLICKED_EMPTY_AREA)

    def __try_cell_click(self, mouse_pos: Tuple) -> bool:

        cell_size = self.coord.cell_size

        for row in self.grid:
            for cell in row:

                x_limit = cell.pos_x + cell_size
                y_limit = cell.pos_y + cell_size

                if (cell.pos_x < mouse_pos[0] < x_limit) and (cell.pos_y < mouse_pos[1] < y_limit):

                    # Cell has been clicked

                    self.selected_cell[0] = cell.row_index
                    self.selected_cell[1] = cell.column_index

                    return True

        self.selected_cell[0] = -1
        self.selected_cell[1] = -1

        return False

    def __try_button_click(self) -> bool:
        # TODO: Add UI buttons
        return False
