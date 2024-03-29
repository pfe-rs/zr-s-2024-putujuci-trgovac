import pygame
import sys

class Circle:
    def __init__(self, color, radius, position):
        self.color = color
        self.radius = radius
        self.position = position

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
class Line:
    def __init__(self, color, start, end, width=1):
        self.color = color
        self.start = start
        self.end = end
        self.width = width

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)