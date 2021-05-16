import pygame
from units import unit

class Raider(unit.Unit):
    """docstring for ."""
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.size = 10

    def tick(self):
        if(self.move()):
            # movement code here
            return
        else:
            #code for not moving
            return
