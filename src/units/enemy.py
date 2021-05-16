import pygame
from units import unit
from config import colors

class Enemy(unit.Unit):
    """docstring for ."""
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
