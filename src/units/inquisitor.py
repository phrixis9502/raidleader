import pygame
from units import raider
from config import colors

class Inquisitor(raider.Raider):
    """docstring for ."""
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.color = colors.Gray
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.move_speed = 5
