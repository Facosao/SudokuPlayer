import constants as const
import pygame
import time


class PencilMark:

    def __init__(self) -> None:
        self.value = 0
        self.FG_color = const.COLOR_PENCIL_MARK


class Cell:  # One instance for each cell on the grid (81 in total)

    def __init__(self, value) -> None:
        self.value = value
        self.fg_color = const.COLOR_USER_NUMBER
        self.bg_color = const.COLOR_WHITE
        self.pos_x = 0
        self.pos_y = 0
        self.row_index = 0
        self.column_index = 0
        self.starting = False
        self.pencil_marks = []

        for i in range(9):
            self.pencil_marks.append(PencilMark())

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
        self.grid: list = grid
        self.selected_cell: list = selected_cell
        self.count = 0
        self.inner_count = 0

    ''' 
        When a cell is deleted, create a event to restore
        regular colors to the rule affected numbers and pencil marks
    '''

    def all_cells(self, mark=0) -> pygame.event.Event:

        selected_row = self.selected_cell[0]
        selected_column = self.selected_cell[1]
        self.count = 0
        self.inner_count = 0

        self.__reset_all_cells_bg()

        if selected_row >= 0 and selected_column >= 0:

            sel_cell = self.grid[selected_row][selected_column]

            if sel_cell.value == 0:

                self.__set_rule_highlight(sel_cell)
                sel_cell.is_selected()

            else:

                self.__set_blocked_cells(sel_cell)
                self.__same_number_highlight(sel_cell)
                sel_cell.is_selected()
                self.__check_for_errors(sel_cell)

        self.__super_check_mark()
        print("count =", self.count)
        print("inner_count =", self.inner_count)
        return pygame.event.post(const.EVENT_REDRAW_CELLS)

    def __reset_all_cells_bg(self) -> None:

        # TODO: Change to NOT erase invalid cells

        for row in self.grid:
            for cell in row:

                if cell.bg_color != const.COLOR_INVALID_NUMBER_BG:
                    cell.default_bg_color()

                if not cell.starting and cell.fg_color != const.COLOR_INVALID_NUMBER_FG:
                    cell.fg_color = const.COLOR_USER_NUMBER

                for mark in cell.pencil_marks:
                    # if mark.FG_color != const.COLOR_INVALID_NUMBER_FG:
                    mark.FG_color = const.COLOR_PENCIL_MARK

    def __set_rule_highlight(self, cell) -> None:

        # Same row
        for column in range(9):
            self.grid[cell.row_index][column].is_rule_highlighted()

        # Same column
        for row in range(9):
            self.grid[row][cell.column_index].is_rule_highlighted()

        # Same 3x3 sub-grid (sg)
        sg_row_start = (cell.row_index // 3) * 3
        sg_row_end = sg_row_start + 3

        sg_column_start = (cell.column_index // 3) * 3
        sg_column_end = sg_column_start + 3

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

        for row in self.grid:
            for cell in row:

                if cell.value == selected_cell.value:
                    cell.same_number_highlight()

    def __check_for_errors(self, sel_cell) -> None:

        sel_row = sel_cell.row_index
        sel_col = sel_cell.column_index
        error_detected = False

        # Error - same row
        for column in range(9):

            test_cell = self.grid[sel_row][column]

            if test_cell.value == sel_cell.value and test_cell.column_index != sel_cell.column_index:
                test_cell.bg_color = const.COLOR_INVALID_NUMBER_BG
                error_detected = True

        # Error - same column
        for row in range(9):

            test_cell = self.grid[row][sel_col]

            if test_cell.value == sel_cell.value and test_cell.row_index != sel_cell.row_index:
                test_cell.bg_color = const.COLOR_INVALID_NUMBER_BG
                error_detected = True

        # Same 3x3 sub-grid (sg)
        sg_row_start = (sel_cell.row_index // 3) * 3
        sg_row_end = sg_row_start + 3

        sg_column_start = (sel_cell.column_index // 3) * 3
        sg_column_end = sg_column_start + 3

        for i in range(sg_row_start, sg_row_end):
            for j in range(sg_column_start, sg_column_end):

                test_cell = self.grid[i][j]

                if test_cell.value == sel_cell.value and \
                        test_cell.row_index != sel_cell.row_index:
                    test_cell.bg_color = const.COLOR_INVALID_NUMBER_BG
                    error_detected = True

        if error_detected is True and sel_cell.starting is False:
            sel_cell.fg_color = const.COLOR_INVALID_NUMBER_FG
        elif error_detected is False and sel_cell.starting is False:
            sel_cell.fg_color = const.COLOR_USER_NUMBER

    def __check_single_mark(self, cell, mark):

        print("Starting single mark check")
        print("mark value =", mark.value, "cell_row: =", cell.row_index, "cell_col =", cell.column_index)

        # Same row
        for column in range(9):
            test_cell = self.grid[cell.row_index][column]
            self.inner_count += 1
            if (mark.value == test_cell.value) and (test_cell.value != 0):
                mark.FG_color = const.COLOR_INVALID_NUMBER_FG
                print("Row error!")
                print("cell.row_index =", cell.row_index, "column =", column)
                print("test_cell_row =", test_cell.row_index, "test_cell_col =", test_cell.column_index)
                return

        # Same column
        for row in range(9):
            test_cell = self.grid[row][cell.column_index]
            self.inner_count += 1
            if (mark.value == test_cell.value) and (test_cell.value != 0):
                mark.FG_color = const.COLOR_INVALID_NUMBER_FG
                print("Column error!")
                print("test_cell_row =", test_cell.row_index, "test_cell_col =", test_cell.column_index)
                return

        sg_row_start = (cell.row_index // 3) * 3
        sg_row_end = sg_row_start + 3

        sg_column_start = (cell.column_index // 3) * 3
        sg_column_end = sg_column_start + 3

        for i in range(sg_row_start, sg_row_end):
            for j in range(sg_column_start, sg_column_end):
                test_cell = self.grid[i][j]
                self.inner_count += 1
                if (mark.value == test_cell.value) and (test_cell.value != 0):
                    mark.FG_color = const.COLOR_INVALID_NUMBER_FG
                    print("Sub-grid error!")
                    print("test_cell_row =", test_cell.row_index, "test_cell_col =", test_cell.column_index)
                    return

    def __super_check_mark(self):

        for row in self.grid:
            for cell in row:

                if cell.value != 0:
                    continue
                self.count += 1
                for mark in cell.pencil_marks:
                    if mark.value != 0 and (mark.FG_color == const.COLOR_PENCIL_MARK):
                        self.__check_single_mark(cell, mark)
