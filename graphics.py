import pygame
import math
from typing import Tuple

import constants as const

class ObjectPosition:

    def __init__(self, screen_res_x, screen_res_y, sudoku_matrix) -> None:
        
        self.screen_x = screen_res_x
        self.screen_y = screen_res_y
 
        self.grid_size           = self.get_grid_size()
        self.grid_x, self.grid_y = self.get_grid_position()

        self.sub_grid_size    = ((self.grid_size - 8) // 3)
        # ((sudoku_x - 2px dividers * 4) // 3 boxes)
        # ---> Total size of 3x3 sub-grid (3 per row, 9 in total)

        self.single_cell_size = math.floor(self.sub_grid_size / 3)

        self.sudoku_matrix: list = sudoku_matrix

        self.generate_cell_position()

    def get_grid_size(self) -> int:

        # Change to be dynamic
        return 509

    def get_grid_position(self) -> Tuple[int, int]:

        grid_pos_x = (self.screen_x - self.grid_size) // 2
        grid_pos_y = (self.screen_y - self.grid_size) // 2

        return grid_pos_x, grid_pos_y

    def generate_cell_position(self) -> None:

        # Same as in graphics.draw_empty_grid()
        R1C1_divider_x = self.grid_x + self.sub_grid_size     + const.THICK_BORDER
        R1C4_divider_x = self.grid_x + self.sub_grid_size * 2 + const.THICK_BORDER * 2
        R4C1_divider_y = self.grid_y + self.sub_grid_size     + const.THICK_BORDER 
        R7C1_divider_y = self.grid_y + self.sub_grid_size * 2 + const.THICK_BORDER * 2

        horizontal_start = [self.grid_x, R1C1_divider_x, R1C4_divider_x]
        vertical_start   = [self.grid_y, R4C1_divider_y, R7C1_divider_y]

        first_cell_offset  = const.THICK_BORDER
        second_cell_offset =  first_cell_offset + self.single_cell_size + const.THIN_BORDER
        third_cell_offset  = second_cell_offset + self.single_cell_size + const.THIN_BORDER

        cell_offset = [first_cell_offset, second_cell_offset, third_cell_offset]

        for i in range(9):
            for j in range(9):

                self.sudoku_matrix[i][j].pos_x = horizontal_start[j // 3] + cell_offset[j % 3]
                self.sudoku_matrix[i][j].pos_y =   vertical_start[i // 3] + cell_offset[i % 3]


def draw_empty_grid(window_surface: pygame.Surface,
                    positions:      ObjectPosition) -> None:

    #grid_size, grid_size = get_grid_size(screen_resolution)
    #grid_x, grid_y = get_grid_position(screen_resolution, (grid_size, grid_size))

    grid_size = positions.grid_size
    grid_x, grid_y = positions.grid_x, positions.grid_y


    SudokuGrid = pygame.Rect(grid_x, grid_y, grid_size, grid_size)
    pygame.draw.rect(window_surface, const.COLOR_GRID_BACKGROUND, SudokuGrid)

    # TODO: Replace raw border constants for named ones
    upper_border_start = (grid_x, grid_y)
    upper_border_end   = ((grid_x + grid_size), grid_y)

    left_border_start = (grid_x, grid_y)
    left_border_end   = (grid_x, (grid_y + grid_size))

    # Check if (-1) is correct
    right_border_start = ((grid_x + grid_size - 1), grid_y)
    right_border_end   = ((grid_x + grid_size - 1), (grid_y + grid_size))

    # Check if (-1) is correct
    lower_border_start = (grid_x, (grid_y + grid_size - 1))
    lower_border_end   = ((grid_x + grid_size), (grid_y + grid_size - 1))

    outer_border_coord = [[upper_border_start, upper_border_end],
                          [ left_border_start,  left_border_end],
                          [right_border_start, right_border_end],
                          [lower_border_start, lower_border_end]]

    sub_grid = ((grid_size - 8) // 3)
    # ((sudoku_x - 2px dividers * 4) // 3 boxes)
    # ---> Total size of 3x3 sub-grid (3 per row, 9 in total)

    first_inner_divider_start = ((grid_x + sub_grid + 2), grid_y)
    first_inner_divider_end   = ((grid_x + sub_grid + 2), (grid_y + grid_size))

    second_inner_divider_start = ((grid_x + sub_grid * 2 + 4), grid_y)
    second_inner_divider_end   = ((grid_x + sub_grid * 2 + 4), (grid_y + grid_size))

    third_inner_divider_start = (grid_x, (grid_y + sub_grid + 2))
    third_inner_divider_end   = ((grid_x + grid_size), (grid_y + sub_grid + 2))

    fourth_inner_divider_start = (grid_x, (grid_y + sub_grid * 2 + 4))
    fourth_inner_divider_end   = ((grid_x + grid_size), (grid_y + sub_grid * 2 + 4))

    inner_divider_coord = [[ first_inner_divider_start,  first_inner_divider_end],
                           [second_inner_divider_start, second_inner_divider_end],
                           [ third_inner_divider_start,  third_inner_divider_end],
                           [fourth_inner_divider_start, fourth_inner_divider_end]]

    for i in range(4):
        pygame.draw.line(window_surface,
                         const.COLOR_GRID_DIVIDER,
                         outer_border_coord[i][0],
                         outer_border_coord[i][1],
                         2)

        pygame.draw.line(window_surface,
                         const.COLOR_GRID_DIVIDER,
                         inner_divider_coord[i][0],
                         inner_divider_coord[i][1],
                         2)

    pygame.display.flip()


def draw_cells(window_surface: pygame.Surface,
               positions:      ObjectPosition,
               sudoku_grid:              list) -> None:

    single_cell_size = positions.single_cell_size

    for row in sudoku_grid:

        for cell in row:

            cell_digit    = str(cell.value) if cell.value != 0 else " "
            cell_fg_color = cell.fg_color
            cell_bg_color = cell.bg_color

            cell_x = cell.pos_x
            cell_y = cell.pos_y

            cell_bg_rect = pygame.Rect(cell_x, cell_y, single_cell_size, single_cell_size)
            pygame.draw.rect(window_surface, cell_bg_color, cell_bg_rect)

            cell_font = pygame.font.SysFont(None, 70) # Change font size to be dynamic
            cell_surface = pygame.font.Font.render(cell_font,
                                                   cell_digit,
                                                   True,
                                                   cell_fg_color,
                                                   cell_bg_color)

            font_x, font_y = cell_font.size(cell_digit)

            cell_centered_x = cell_x + ((single_cell_size - font_x) // 2)
            cell_centered_y = cell_y + ((single_cell_size - font_y) // 2)

            cell_digit_rect = cell_surface.get_rect(topleft=(cell_centered_x,
                                                             cell_centered_y),
                                                    width=single_cell_size,
                                                    height=single_cell_size)

            window_surface.blit(cell_surface, cell_digit_rect)

    pygame.display.flip()

def draw_clock(window_surface: pygame.Surface,
               clock_string:              str) -> None:

    clock_font = pygame.font.SysFont(None, 40) # Change font size to be dynamic
    clock_surface = pygame.font.Font.render(clock_font, clock_string, True, const.COLOR_BLACK, const.COLOR_WHITE)
    
    clock_size_x, clock_size_y = clock_font.size(clock_string)

    clock_rect = clock_surface.get_rect(topleft=(0, 0),
                                        width=clock_size_x,
                                        height=clock_size_y)

    window_surface.blit(clock_surface, clock_rect)
    pygame.display.flip()

def draw_complete_frame(window_surface: pygame.Surface,
                        clock_string:              str,
                        positions:      ObjectPosition,
                        sudoku_grid:              list) -> None:

    window_surface.fill(const.COLOR_WHITE)
    draw_empty_grid(window_surface, positions)
    draw_cells(window_surface, positions, sudoku_grid)
    draw_clock(window_surface, clock_string)
    #pygame.display.flip()