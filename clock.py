from time import time
from math import floor


class Clock:

    def __init__(self) -> None:
        self.initial_time = floor(time())

    def generate_clock_str(self) -> str:

        current_time = floor(time())
        current_time -= self.initial_time

        clock_temp = [current_time // 3600, current_time // 60, current_time % 60]

        for j in range(3):

            if clock_temp[j] < 10:
                clock_temp[j] = "0" + str(clock_temp[j])
            else:
                clock_temp[j] = str(clock_temp[j])

        clock_str = clock_temp[1] + ":" + clock_temp[2]

        if clock_temp[0] != "00":
            clock_str = clock_temp[0] + ":" + clock_str

        return clock_str
