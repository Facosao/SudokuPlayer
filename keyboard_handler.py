import pygame
import graphics
import constants as const

class KeyboardHandler():

    def __init__(self, grid, selected_cell) -> None:
        self.grid:     list = grid
        self.sel_cell: list = selected_cell

    def try_all_keys(self, key):

        if pygame.K_1 <= key <= pygame.K_9:

            print("key =", key)
            
            sel_row = self.sel_cell[0]
            sel_col = self.sel_cell[1]

            cell = self.grid[sel_row][sel_col]

            if sel_row >= 0 and sel_col >= 0:

                if cell.starting == False:

                    # Insert number
                    cell.value = key - 48
                    cell.fg_color = const.COLOR_USER_CELL

            pygame.event.post(const.EVENT_CLICKED_CELL)

        elif key == pygame.K_w:
            pygame.event.post(pygame.QUIT)