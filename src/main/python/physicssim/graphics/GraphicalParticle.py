from enum import Enum
from math import sqrt

import pygame


class Charge(Enum):
    POSITIVE = 1
    NEGATIVE = 2

class GraphicalParticle:
    def __init__(self, center, radius, charge, color=(255, 0, 0), moveState=False):
        self.center = center
        self.radius = radius
        self.charge = charge
        self.color = color
        self.moveState = moveState
        
    def update(self, center, radius, charge, color=(255, 0, 0)):
        self.center = center
        self.radius = radius
        self.charge = charge
        self.color = color

    def draw(self, screen):
        #particleSurface = pygame.Surface((self.radius * 2, self.radius * 2))
        pygame.draw.circle(screen, self.color, (int(self.center[0]), int(self.center[1])), int(self.radius))
        #screen.blit(particleSurface, (self.center[0] - self.radius, self.center[1] - self.radius))
        
    def mouseCollision(self, event):
        mouseDistance = sqrt((event.pos[0] - self.center[0]) ** 2 + (event.pos[1] - self.center[1]) ** 2)
        return mouseDistance <= self.radius