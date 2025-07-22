import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, SHOT_RADIUS
from bullet import Bullet

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation +90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, deltatime):
        self.rotation += PLAYER_TURN_SPEED * deltatime

    def move(self, deltatime):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * deltatime

    def shoot(self):
        if self.timer > 0:
            return
        bullet = Bullet(self.position.x, self.position.y, SHOT_RADIUS)
        velocity = (pygame.Vector2(0, 1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED
        bullet.velocity = velocity
        self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, deltatime):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-deltatime)
        if keys[pygame.K_d]:
            self.rotate(deltatime)
        if keys[pygame.K_w]:
            self.move(deltatime)
        if keys[pygame.K_s]:
            self.move(-deltatime)
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.timer > 0:
            self.timer -= deltatime