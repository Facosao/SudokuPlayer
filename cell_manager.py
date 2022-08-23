import copy

import pygame
import constants as const


class CellManager:

    def __init__(self, grid, selected_cell) -> None:

        self.grid: list = grid
        self.sel_cell: list = selected_cell

    def insert_number(self, number):

        sel_row = self.sel_cell[0]
        sel_col = self.sel_cell[1]

        cell = self.grid[sel_row][sel_col]
        #print("inserted number =", cell.value)
        pencil_mark = 0

        if sel_row >= 0 and sel_col >= 0 and cell.starting is False:

            old_cell = copy.deepcopy(cell)
            undo_event = pygame.event.Event(const.ID_UNDO_PUSH, old_cell=old_cell)
            pygame.event.post(undo_event)

            if number > 9:  # Pencil Mark

                number -= 10
                index = number - 1
                value = cell.pencil_marks[index].value

                if value == 0:
                    cell.pencil_marks[index].value = number
                    pencil_mark = number
                else:
                    cell.pencil_marks[index].value = 0

            else:

                cell.value = number

            event = pygame.event.Event(const.ID_INSERTED_NUMBER, mark=pencil_mark)
            pygame.event.post(event)

    def delete_number(self):

        sel_row = self.sel_cell[0]
        sel_col = self.sel_cell[1]

        cell = self.grid[sel_row][sel_col]

        if sel_row >= 0 and sel_col >= 0 and cell.starting is False:

            cell.value = 0

            for i in range(9):
                cell.pencil_marks[i].value = 0

            pygame.event.post(const.EVENT_SELECTED_CELL)

    def change_selected_cell(self, direction: str):

        sel_row = self.sel_cell[0]
        sel_col = self.sel_cell[1]

        # Acts as a mouse click on a adjacent cell
        # TODO: Replace string with named constants (?)

        if direction == "Up":

            if self.sel_cell[0] > 0:

                self.sel_cell[0] = sel_row - 1
                pygame.event.post(const.EVENT_SELECTED_CELL)

        elif direction == "Down":

            if self.sel_cell[0] < 8:

                self.sel_cell[0] = sel_row + 1
                pygame.event.post(const.EVENT_SELECTED_CELL)

        elif direction == "Left":

            if self.sel_cell[1] > 0:

                self.sel_cell[1] = sel_col - 1
                pygame.event.post(const.EVENT_SELECTED_CELL)

        elif direction == "Right":

            if self.sel_cell[1] < 8:

                self.sel_cell[1] = sel_col + 1
                pygame.event.post(const.EVENT_SELECTED_CELL)
