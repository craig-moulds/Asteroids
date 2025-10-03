from circleshape import *
import pygame

class Shot(CircleShape):
    SHOT_RADIUS = 5
    SHOT_SPEED = 500

    def __init__(self, x, y):
        super().__init__(x, y, self.SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), 
                            int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
