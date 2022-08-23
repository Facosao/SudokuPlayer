import pygame
import constants as const
import sudoku
import time


class UndoObject:

    def __init__(self, cell, sel_cell_tuple):
        self.cell: sudoku.Cell = cell
        self.sel_cel_tuple = sel_cell_tuple


class Undo:

    def __init__(self, game_grid, selected_cell):

        self.grid: list = game_grid
        self.sel_cell: list = selected_cell
        self.stack: list = []

    def push(self, old_cell):

        sel_cell_tuple = (self.sel_cell[0], self.sel_cell[1])

        self.stack.append(UndoObject(old_cell, sel_cell_tuple))

    def pop(self):

        try:

            old_obj: UndoObject = self.stack.pop()

            old_row, old_col = old_obj.sel_cel_tuple[0], old_obj.sel_cel_tuple[1]
            old_cell = old_obj.cell

            # self.grid[old_row][old_col] = old_cell
            self.sel_cell[0], self.sel_cell[1] = old_row, old_col

            #print("old_cell = %d" % self.grid[old_row][old_col].value)
            #print("temp_value = %d" % old_cell.value)

            self.grid[old_row][old_col].value = old_cell.value
            self.grid[old_row][old_col].pencil_marks = old_cell.pencil_marks

            #print("new_cell = %d" % self.grid[old_row][old_col].value)

            pygame.event.post(const.EVENT_SELECTED_CELL)

        except IndexError:

            #print("Global stack is empty!", time.time())
            return
