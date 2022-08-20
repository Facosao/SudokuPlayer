import pygame
import constants as const

class CellManager:

    def __init__(self, grid, selected_cell) -> None:
        self.grid:     list = grid
        self.sel_cell: list = selected_cell

    def insert_number(self, number):

        sel_row = self.sel_cell[0]
        sel_col = self.sel_cell[1]

        cell = self.grid[sel_row][sel_col]

        if sel_row >= 0 and sel_col >= 0 and cell.starting == False:

            cell.value    = number
            cell.fg_color = const.COLOR_USER_NUMBER
            
            pygame.event.post(const.EVENT_SELECTED_CELL)

    def delete_number(self):

        sel_row = self.sel_cell[0]
        sel_col = self.sel_cell[1]

        cell = self.grid[sel_row][sel_col]

        if sel_row >= 0 and sel_col >= 0 and cell.starting == False:

            cell.value = 0
            pygame.event.post(const.EVENT_SELECTED_CELL)

    def change_selected_cell(self, direction: str):

        sel_row = self.sel_cell[0]
        sel_col = self.sel_cell[1]

        # Acts as a mouse click on a adjacent cell
        # TODO: Replace string with named constants (?)

        if direction == "Up":

            if self.sel_cell[0] > 0:

                self.sel_cell.pop()
                self.sel_cell.pop()
                self.sel_cell.append(sel_row - 1)
                self.sel_cell.append(sel_col)

                pygame.event.post(const.EVENT_SELECTED_CELL)

        elif direction == "Down":

            if self.sel_cell[0] < 8:

                self.sel_cell.pop()
                self.sel_cell.pop()
                self.sel_cell.append(sel_row + 1)
                self.sel_cell.append(sel_col)

                pygame.event.post(const.EVENT_SELECTED_CELL)

        elif direction == "Left":

            if self.sel_cell[1] > 0:

                self.sel_cell.pop()
                self.sel_cell.append(sel_col - 1)

                pygame.event.post(const.EVENT_SELECTED_CELL)

        elif direction == "Right":

            if self.sel_cell[1] < 8:

                self.sel_cell.pop()
                self.sel_cell.append(sel_col + 1)

                pygame.event.post(const.EVENT_SELECTED_CELL)
