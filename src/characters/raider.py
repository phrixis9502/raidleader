import pygame
from characters import unit

class Raider(unit.Unit):
    """docstring for ."""
    def __init__(self):
        super().__init__()
        self.size = 10
        self.x_pos = 100
        self.y_pos = 100
