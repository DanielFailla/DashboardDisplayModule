from Timer import *
import math

class IndicatorController():
    def __init__(self, period):
        self._period = period
        self._timer = Timer()

    def Restart(self):
        self._timer.Reset()
    
    def IsActive(self):
        if self._timer < (self._period/2):
            return True
        elif self._timer < self._period:
            return False
        elif self._timer > self._period:
            self._timer -= self._period*math.floor(self._timer / self._period)
            return self.IsActive();
