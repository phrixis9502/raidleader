from math import sin, cos
from numpy import arctan
import pygame

class Raider():
    """docstring for ."""

    def __init__(self):
        self.x_pos = 1
        self.y_pos = 1
        self.x_dest = self.x_pos
        self.y_dest = self.y_pos
        self.move_speed = 3

    def move(self):
        if (self.x_pos != self.x_dest) & (self.y_pos != self.y_dest): #Force int for this comparison
            dx = self.x_dest - self.x_pos
            dy = self.y_dest - self.y_pos
            angle = arctan(dy/dx) #This math is bad, cannot be negative x
            self.x_pos = self.x_pos + (cos(angle) * self.move_speed)
            self.y_pos = self.y_pos + (sin(angle) * self.move_speed)

    def set_destination(self, x, y):
        self.x_dest = x
        self.y_dest = y

    def render(self, DisplaySurface):
        pygame.draw.circle(DisplaySurface, (155,155,155), (self.x_pos, self.y_pos), 2,  )
