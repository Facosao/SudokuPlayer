from typing import Tuple
import constants as const
import graphics

class Cell: # One instance for each cell on the grid (81 in total)

    def __init__(self, value, fg_color, bg_color) -> None:
        
        self.value = value
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.pos_x = 0
        self.pos_y = 0
        self.cell_row_index = 0
        self.cell_column_index = 0

    def is_selected(self) -> None:
        self.bg_color = const.COLOR_SELECTED_CELL

    def same_number_highlight(self) -> None:
        self.bg_color = const.COLOR_SAME_NUMBER

    def is_rule_highlighted(self) -> None:
        self.bg_color = const.COLOR_RULE_HIGHLIGHT

    def default_bg_color(self) -> None:
        self.bg_color = const.COLOR_WHITE 

def reset_all_cells_bg(sudoku_grid) -> None:

    for row in sudoku_grid:

        for cell in row:

            cell.default_bg_color()

def set_rule_highlight(cell_row:    int,
                       cell_column: int,
                       sudoku_grid: list) -> None:

    # Same row
    for i in range(9):
        sudoku_grid[cell_row][i].is_rule_highlighted()

    # Same column
    for i in range(9):
        sudoku_grid[i][cell_column].is_rule_highlighted()

    # Same 3x3 sub-grid (sg)
    sg_row_start = (cell_row // 3) * 3
    sg_row_end   = sg_row_start + 3

    sg_column_start = (cell_column // 3) * 3
    sg_column_end   = sg_column_start + 3

    for i in range(sg_row_start, sg_row_end):
        for j in range(sg_column_start, sg_column_end):

            sudoku_grid[i][j].is_rule_highlighted()

def set_blocked_cells(number:       int,
                      sudoku_grid: list) -> None:

    #if source_cell.value == 0:
        #set_rule_highlight(cell_row_index,
        #                   cell_column_index,
        #                   sudoku_grid)
    #    pass
                          
    for i in range(9):
        for j in range(9):
        
            cell = sudoku_grid[i][j]
            
            if cell.value == number and cell.value != 0:
                set_rule_highlight(i, j, sudoku_grid)
            elif cell.value != number and cell.value != 0:
                cell.is_rule_highlighted()

def same_number_highlight(number:       int,
                          sudoku_grid: list) -> None:

    if number == 0:
        return
                
    for row in sudoku_grid:

        for cell in row:
            
            if cell.value == number:
                cell.same_number_highlight()

def check_click_pos(mouse_pos: Tuple[int, int],
                    sudoku_grid: list,
                    positions: graphics.UICoordinates) -> int:
    
    cell_size = positions.cell_size

    for i in range(9):
        for j in range(9):

            cell = sudoku_grid[i][j]

            x_limit = cell.pos_x + cell_size
            y_limit = cell.pos_y + cell_size

            if (cell.pos_x < mouse_pos[0] < x_limit) and\
               (cell.pos_y < mouse_pos[1] < y_limit):

                reset_all_cells_bg(sudoku_grid)
                set_blocked_cells(cell.value, sudoku_grid)
                same_number_highlight(cell.value, sudoku_grid)
                cell.is_selected()

                return const.SP_REDRAW_CELLS

    return const.SP_CONTINUE
