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
    def __init__(self, x, y, speed, texture, w, h):
        super().__init__(x, y, speed, texture, w, h)
        self.x = x
        self.direction = "forward"

    def update(self):
        self.hitbox.y += self.speed
        if self.hitbox.y >= 650:
            self.x = random.randint(100, 700)
            self.hitbox.y = -150

class Rocket(BaseSprite):
    def __init__(self, x, y, speed, texture, w, h):
        super().__init__(x, y, speed, texture, w, h)
        self.bullets = []
    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
        if keys[pygame.K_SPACE]:
            self.bullets.append(Bullet(self.hitbox.x + 10, self.hitbox.y, 4, "assets/bullet.png", 5, 10))
class Meteor:
    def __init__(self, x, y):
        self.texture = pygame.image.load("assets/asteroid.png")
        self.texture = pygame.transform.scale(self.texture, [60, 60])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
    def draw(self, window):
        window.blit(self.texture, self.hitbox)

class Bullet:
    def __init__(self, x, y, speed, texture, w, h):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [w, h])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed




    def draw(self, window):
        window.blit(self.texture, self.hitbox)
pygame.init()

window = pygame.display.set_mode([800, 600])
background_img = pygame.image.load("assets/galaxy.jpg")
background_img = pygame.transform.scale(background_img, [800, 600])
fps = pygame.time.Clock()
rocket = Rocket(400, 520, 5, "assets/rocket.png", 30, 70)
meteors = [Meteor(225, 200), Meteor(400, 125)]

enemies = []
y = 50
for i in range(10):
    x = random.randint(100, 700)
    enemies.append(Ufo(x, y, 5, 'assets/ufo. png', 60, 40))
    y -= 100

running = True

while running:
    window.blit(background_img, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for meteor in meteors:
        meteor.draw(window)
    for enemy in enemies:
        enemy.draw(window)
        enemy.update()
        print(enemy.hitbox.y)
    for bullet in rocket.bullets[:]:
        bullet.draw(window)
        bullet.update()
        for enemy in enemies:
            if bullet.hitbox.colliderect(enemy.hitbox):
                rocket.bullets.remove(bullet)
                enemy.hitbox.y = -100
                enemy.hitbox.x = random.randint(100, 700)
    rocket.draw(window)
    rocket.control()
    pygame.display.flip()
    fps.tick(60)

