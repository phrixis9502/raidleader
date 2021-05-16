import pygame
from units import raider
from config import colors

class Inquisitor(unit.Raider):
    """docstring for ."""
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.color = colors.Gray
