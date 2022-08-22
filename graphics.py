import pygame
from typing import Tuple
import constants as const


class UICoordinates:

    def __init__(self, screen_res_x, screen_res_y, sudoku_matrix) -> None:

        self.screen_x = screen_res_x
        self.screen_y = screen_res_y

        self.grid_size = self.get_grid_size()
        self.grid_x, self.grid_y = self.get_grid_position()

        # Total size of 3x3 sub-grid (3 per row, 9 in total)
        self.sub_grid_size = ((self.grid_size - const.OUTER_BORDER * 4) // 3)

        self.cell_size = self.sub_grid_size // 3

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

        # Duplicate from DrawBoard.__draw_empty_grid()
        r1_c1_divider_x = self.grid_x + self.sub_grid_size + const.OUTER_BORDER
        r1_c4_divider_x = self.grid_x + self.sub_grid_size * 2 + const.OUTER_BORDER * 2
        r4_c1_divider_y = self.grid_y + self.sub_grid_size + const.OUTER_BORDER
        r7_c1_divider_y = self.grid_y + self.sub_grid_size * 2 + const.OUTER_BORDER * 2

        horizontal_start = [self.grid_x, r1_c1_divider_x, r1_c4_divider_x]
        vertical_start = [self.grid_y, r4_c1_divider_y, r7_c1_divider_y]

        first_cell_offset = const.OUTER_BORDER
        second_cell_offset = first_cell_offset + self.cell_size + const.CELL_BORDER
        third_cell_offset = second_cell_offset + self.cell_size + const.CELL_BORDER

        cell_offset = [first_cell_offset, second_cell_offset, third_cell_offset]

        for i in range(9):
            for j in range(9):
                self.sudoku_matrix[i][j].pos_x = horizontal_start[j // 3] + cell_offset[j % 3]
                self.sudoku_matrix[i][j].pos_y = vertical_start[i // 3] + cell_offset[i % 3]


class DrawBoard:

    def __init__(self, surface, ui_coord) -> None:

        self.surface: pygame.Surface = surface
        self.coord: UICoordinates = ui_coord

    def __draw_empty_grid(self) -> None:

        grid_size = self.coord.grid_size
        grid_x, grid_y = self.coord.grid_x, self.coord.grid_y

        sudoku_grid = pygame.Rect(grid_x, grid_y, grid_size, grid_size)
        pygame.draw.rect(self.surface, const.COLOR_GRID_BACKGROUND, sudoku_grid)

        upper_border_start = (grid_x, grid_y)
        upper_border_end = ((grid_x + grid_size), grid_y)

        left_border_start = (grid_x, grid_y)
        left_border_end = (grid_x, (grid_y + grid_size))

        # Check if (-1) is correct
        right_border_start = ((grid_x + grid_size - 1), grid_y)
        right_border_end = ((grid_x + grid_size - 1), (grid_y + grid_size))

        # Check if (-1) is correct
        lower_border_start = (grid_x, (grid_y + grid_size - 1))
        lower_border_end = ((grid_x + grid_size), (grid_y + grid_size - 1))

        grid_border_coord = [[upper_border_start, upper_border_end],
                             [left_border_start, left_border_end],
                             [right_border_start, right_border_end],
                             [lower_border_start, lower_border_end]]

        # Total size of 3x3 sub-grid (3 per row, 9 in total)
        sub_grid = ((grid_size - const.OUTER_BORDER * 4) // 3)

        # R1C1 -> Row 1, Column 1 (from left to right, top to bottom)
        r1c1_divider_start = ((grid_x + sub_grid + 2), grid_y)
        r1_c1_divider_end = ((grid_x + sub_grid + 2), (grid_y + grid_size))

        r1_c4_divider_start = ((grid_x + sub_grid * 2 + 4), grid_y)
        r1_c4_divider_end = ((grid_x + sub_grid * 2 + 4), (grid_y + grid_size))

        r4_c1_divider_start = (grid_x, (grid_y + sub_grid + 2))
        r4_c1_divider_end = ((grid_x + grid_size), (grid_y + sub_grid + 2))

        r7_c1_divider_start = (grid_x, (grid_y + sub_grid * 2 + 4))
        r7_c1_divider_end = ((grid_x + grid_size), (grid_y + sub_grid * 2 + 4))

        cell_divider_coord = [[r1c1_divider_start, r1_c1_divider_end],
                              [r1_c4_divider_start, r1_c4_divider_end],
                              [r4_c1_divider_start, r4_c1_divider_end],
                              [r7_c1_divider_start, r7_c1_divider_end]]

        for i in range(4):
            pygame.draw.line(self.surface,
                             const.COLOR_GRID_DIVIDER,
                             grid_border_coord[i][0],
                             grid_border_coord[i][1],
                             2)

            pygame.draw.line(self.surface,
                             const.COLOR_GRID_DIVIDER,
                             cell_divider_coord[i][0],
                             cell_divider_coord[i][1],
                             2)

    def draw_cells(self, grid: list):

        cell_size = self.coord.cell_size

        for row in grid:
            for cell in row:

                digit = str(cell.value)
                fg_color = cell.fg_color
                bg_color = cell.bg_color

                x = cell.pos_x
                y = cell.pos_y

                bg_rect = pygame.Rect(x, y, cell_size, cell_size)
                pygame.draw.rect(self.surface, bg_color, bg_rect)

                if cell.value == 0:
                    self.__draw_pencil_marks(cell)
                    continue

                # Change font size to be dynamic
                font = pygame.font.SysFont(None, 70)
                surface = font.render(digit, True, fg_color, bg_color)

                font_width, font_height = font.size(digit)

                centered_x = x + ((cell_size - font_width) // 2)
                centered_y = y + ((cell_size - font_height) // 2) + 2

                digit_rect = surface.get_rect(topleft=(centered_x, centered_y),
                                              width=cell_size,
                                              height=cell_size)

                self.surface.blit(surface, digit_rect)

        return pygame.event.post(const.EVENT_FLIP_BUFFER)

    def __draw_pencil_marks(self, cell):

        bg_color = cell.bg_color

        cell_size = self.coord.cell_size
        mark_size = cell_size // 3

        one_mark_x = cell.pos_x
        two_mark_x = one_mark_x + mark_size
        three_mark_x = two_mark_x + mark_size

        one_mark_y = cell.pos_y
        two_mark_y = one_mark_y + mark_size
        three_mark_y = two_mark_y + mark_size

        hor_mark = [one_mark_x, two_mark_x, three_mark_x]
        ver_mark = [one_mark_y, two_mark_y, three_mark_y]

        font = pygame.font.SysFont(None, 27)

        for i in range(9):
            mark = cell.pencil_marks[i]
            fg_color = mark.FG_color

            digit = str(mark.value) if mark.value != 0 else ""
            surface = font.render(digit, True, fg_color, bg_color)

            font_width, font_height = font.size(digit)

            left = hor_mark[i % 3]
            top = ver_mark[i // 3]

            centered_left = left + ((mark_size - font_width) // 2)
            centered_top = top + ((mark_size - font_height) // 2) + 1

            rect = surface.get_rect(topleft=(centered_left, centered_top), width=font_width, height=font_height)

            self.surface.blit(surface, rect)

        return pygame.event.post(const.EVENT_FLIP_BUFFER)

    def draw_clock(self, clock_str: str):

        # Change font size to be dynamic
        font = pygame.font.SysFont(None, 40)
        surface = font.render(clock_str, True, const.COLOR_BLACK, const.COLOR_WHITE)

        font_width, font_height = font.size(clock_str)

        rect = surface.get_rect(topleft=(0, 0), width=font_width, height=font_height)

        self.surface.blit(surface, rect)

        return pygame.event.post(const.EVENT_FLIP_BUFFER)

    def draw_complete_frame(self, grid, clock_str):

        self.surface.fill(const.COLOR_WHITE)
        self.__draw_empty_grid()
        self.draw_cells(grid)
        self.draw_clock(clock_str)

        return pygame.event.post(const.EVENT_FLIP_BUFFER)
