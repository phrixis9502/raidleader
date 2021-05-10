import pygame
import numpy as np

class Unit():
    """docstring for ."""
    def __init__(self):
        self.x_pos = 1
        self.y_pos = 1
        self.dest = []
        self.move_speed = 5
        self.color = (155,155,155)

    def move(self):
        if len(self.dest) != 0:
            dx = self.x_pos - self.dest[0][0]
            dy = self.y_pos - self.dest[0][1]
            distance = np.sqrt(np.sum(np.power([dx,dy], 2)))
            if distance <= self.move_speed:
                self.x_pos = self.dest[0][0]
                self.y_pos = self.dest[0][1]
                self.dest.pop(0)
            else:
                ratio = self.move_speed / distance
                self.x_pos = self.x_pos - (dx * ratio)
                self.y_pos = self.y_pos - (dy * ratio)

    def set_destination(self, coords):
        self.dest.append(coords)

    def clear_destination(self):
        self.dest = []

    def render(self, DisplaySurface):
        pygame.draw.circle(DisplaySurface, self.color, (self.x_pos, self.y_pos), self.size)
