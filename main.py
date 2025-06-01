import pygame
import random

class BaseSprite:
    def __init__(self, x, y, speed, texture, w, h):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [w, h])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self, window):
        window.blit(self.texture, self.hitbox)

class Ufo(BaseSprite):
    def __init__(self, x, y, speed, texture, w, h, target_x, target_y):
        super().__init__(x, y, speed, texture, w, h)
        self.x = x
        self.direction = "forward"
        self.target_x = target_x

    def update(self):
        if self.direction == "forward":
            self.hitbox.x += self.speed
            if self.hitbox.x >= self.target_x:
                self.direction = "backward"
        else:
            self.hitbox.x -= self.speed
            if self.hitbox.x <= self.x:
                self.direction = "forward"

class Rocket(BaseSprite):
    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed

class Meteor():
    def __init__(self, x, y, texture, w, h):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [60, 60])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

pygame.init()

window = pygame.display.set_mode([800, 600])
background_img = pygame.image.load("assets/galaxy.jpg")
background_img = pygame.transform.scale(background_img, [800, 600])
fps = pygame.time.Clock()
ufo = Ufo(400, 200, 5, "assets/ufo.png", 50, 30, 550, 200)
rocket = Rocket(400, 520, 5, "assets/rocket.png", 30, 70)

running = True

while running:
    window.blit(background_img, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    ufo.draw(window)
    ufo.update()
    rocket.draw(window)
    rocket.control()
    pygame.display.flip()
    fps.tick(60)

