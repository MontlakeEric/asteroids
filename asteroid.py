import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MAX_RADIUS, ASTEROID_MAX_SCORE, ASTEROID_MIN_SCORE

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.color = (random.randint(80, 255), random.randint(80, 255), random.randint(80, 255))
        self.score = ASTEROID_MAX_SCORE - ((int(self.radius / ASTEROID_MIN_RADIUS) - 1) * ASTEROID_MIN_SCORE)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

        if (self.position.x < -ASTEROID_MAX_RADIUS or self.position.x > SCREEN_WIDTH + ASTEROID_MAX_RADIUS or
            self.position.y < -ASTEROID_MAX_RADIUS or self.position.y > SCREEN_HEIGHT + ASTEROID_MAX_RADIUS):
            self.kill()

    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        log_event("asteroid_split")
        angle_change = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(angle_change)
        new_velocity2 = self.velocity.rotate(-angle_change)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid1.color = self.color
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2 * 1.2
        asteroid2.color = self.color