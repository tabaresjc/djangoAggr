# -*- coding: utf-8 -*-
import time

class TimerHelper:

    def __init__(self):
        self.start = time.time()

    @property
    def seconds(self):
        end = time.time()
        return (end - self.start) % 60
