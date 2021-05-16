import pygame
from units import enemy
from config import colors

class Boss(enemy.Enemy):
    """docstring for ."""
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.size = 30
        self.color = colors.Red
