import pygame
import time
import constants as const

class KeyboardHandler():

    def __init__(self, grid, selected_cell) -> None:
        self.grid:          list = grid
        self.sel_cell:      list = selected_cell
        self.pressed_ctrl:  bool = False
        self.pressed_shift: bool = False

    def key_released(self, key):

        if key == pygame.K_LCTRL or key == pygame.K_RCTRL:
            self.pressed_ctrl = False

        elif key == pygame.K_LSHIFT or key == pygame.K_RSHIFT:
            self.pressed_shift = False

    def try_all_keys(self, key):

        if pygame.K_1 <= key <= pygame.K_9:

            num = key - pygame.K_0

            if self.pressed_shift == True:
                # Pencil mark
                #print("Pressed Shift + %d!" % (num), time.time())
                num += 10

            event = pygame.event.Event(const.ID_EDIT_CELL, number=num)
            return pygame.event.post(event)

        elif pygame.K_KP1 <= key <= pygame.K_KP9:

            num = key - pygame.K_KP0 + 10

            if self.pressed_shift == True:
                # Pencil mark
                #print("Pressed Shift + %d!" % (num), time.time())
                num += 10

            event = pygame.event.Event(const.ID_EDIT_CELL, number=num)
            return pygame.event.post(event)

        elif key == pygame.K_DELETE or key == pygame.K_BACKSPACE:

            return pygame.event.post(const.EVENT_DELETE_CELL)

        elif key == pygame.K_UP:

            event = pygame.event.Event(const.ID_MOVE_SEL_CELL, direction="Up")
            return pygame.event.post(event)

        elif key == pygame.K_DOWN:

            event = pygame.event.Event(const.ID_MOVE_SEL_CELL, direction="Down")
            return pygame.event.post(event)

        elif key == pygame.K_LEFT:

            event = pygame.event.Event(const.ID_MOVE_SEL_CELL, direction="Left")
            return pygame.event.post(event)

        elif key == pygame.K_RIGHT:

            event = pygame.event.Event(const.ID_MOVE_SEL_CELL, direction="Right")
            return pygame.event.post(event)

        elif key == pygame.K_w:

            event = pygame.event.Event(pygame.QUIT)
            return pygame.event.post(event)

        elif key == pygame.K_LCTRL or key == pygame.K_RCTRL:

            self.pressed_ctrl = True

        elif key == pygame.K_LSHIFT or key == pygame.K_RSHIFT:

            self.pressed_shift = True

        elif key == pygame.K_z:

            if self.pressed_ctrl == True:
                return print("Pressed Ctrl+Z!", time.time())
