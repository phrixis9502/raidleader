import pygame
from units import unit
from config import color

class Enemy(unit.Unit):
    """docstring for ."""
    def __init__(self):
        super().__init__()
        self.size = 30
        self.x_pos = 300
        self.y_pos = 300
        self.color = color.Red
