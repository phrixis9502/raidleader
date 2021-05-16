import pygame
import numpy as np
from config import colors

class Unit():
    """docstring for ."""
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dest = []
        # move_speed - Set in subclass
        # color - Set in subclass
        # hit_points - Set in subclass

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
            return True
        else:
            return False

    def set_destination(self, coords):
        self.dest.append(coords)

    def clear_destination(self):
        self.dest = []

    def render(self, display_surface):
        pygame.draw.circle(display_surface, self.color, (self.x_pos, self.y_pos), self.size)

    def render_highlights():
        pygame.draw.circle(display_surface, colors.yellow, (self.x_pos, self.y_pos), self.size / 2)
