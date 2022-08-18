from typing import Tuple
import constants as const
import graphics
import pygame

class Cell: # One instance for each cell on the grid (81 in total)

    def __init__(self, value, fg_color, bg_color) -> None:
        
        self.value = value
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.pos_x = 0
        self.pos_y = 0
        self.row_index = 0
        self.column_index = 0

    def is_selected(self) -> None:
        self.bg_color = const.COLOR_SELECTED_CELL

    def same_number_highlight(self) -> None:
        self.bg_color = const.COLOR_SAME_NUMBER

    def is_rule_highlighted(self) -> None:
        self.bg_color = const.COLOR_RULE_HIGHLIGHT

    def default_bg_color(self) -> None:
        self.bg_color = const.COLOR_WHITE


class HighlightCells:

    def __init__(self, grid: list, selected_cell: list) -> None:
        self.grid:          list = grid
        self.selected_cell: list = selected_cell

    def all_cells(self) -> pygame.event.Event:

        selected_row    = self.selected_cell[0]
        selected_column = self.selected_cell[1]

        self.__reset_all_cells_bg()
            
        if selected_row >= 0 and selected_column >= 0:

            sel_cell = self.grid[selected_row][selected_column]

            if sel_cell.value == 0:
                    self.__set_rule_highlight(sel_cell)

            else:
                self.__set_blocked_cells(sel_cell)
            
            self.__same_number_highlight(sel_cell)

        return pygame.event.post(const.EVENT_REDRAW_CELLS)

    def __reset_all_cells_bg(self) -> None:

        for row in self.grid:
            for cell in row:
                cell.default_bg_color()

    def __set_rule_highlight(self, cell) -> None:

        # Same row
        for column in range(9):
            self.grid[cell.row_index][column].is_rule_highlighted()

        # Same column
        for row in range(9):
            self.grid[row][cell.column_index].is_rule_highlighted()

        # Same 3x3 sub-grid (sg)
        sg_row_start = (cell.row_index // 3) * 3
        sg_row_end   = sg_row_start + 3

        sg_column_start = (cell.column_index // 3) * 3
        sg_column_end   = sg_column_start + 3

        for i in range(sg_row_start, sg_row_end):
            for j in range(sg_column_start, sg_column_end):

                self.grid[i][j].is_rule_highlighted()

    def __set_blocked_cells(self, selected_cell) -> None:
                          
        number = selected_cell.value

        for row in self.grid:
            for cell in row:

                if cell.value == number and cell.value != 0:
                    self.__set_rule_highlight(cell)

                elif cell.value != number and cell.value != 0:
                    cell.is_rule_highlighted()

    def __same_number_highlight(self, selected_cell) -> None:

        if selected_cell.value == 0: 
            return
                    
        for row in self.grid:
            for cell in row:
                
                if cell.value == selected_cell.value:
                    cell.same_number_highlight()
