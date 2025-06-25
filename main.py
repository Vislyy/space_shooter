import pygame
import random
from saving_manager import *

missed_enemies = 0
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
        global missed_enemies
        self.hitbox.y += self.speed
        if self.hitbox.y >= 650:
            self.x = random.randint(100, 700)
            self.hitbox.y = -150
            missed_enemies += 1

class Rocket(BaseSprite):
    def __init__(self, x, y, speed, texture, w, h):
        super().__init__(x, y, speed, texture, w, h)
        self.bullets = []
        self.fire = pygame.mixer.Sound("assets/fire.ogg")
        self.attack_cooldown = 1000
        self.can_shoot = False
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
        if keys[pygame.K_SPACE] and self.can_shoot:
            self.bullets.append(Bullet(self.hitbox.x + 10, self.hitbox.y, 4, "assets/bullet.png", 5, 10))
            self.fire.play()
            self.can_shoot = False
            self.attack_cooldown = 1000

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 20

        if self.attack_cooldown <= 0:
            self.can_shoot = True


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

    def update(self):
        self.hitbox.y -= self.speed

def start_game():
    global missed_enemies
    pygame.init()
    pygame.mixer.init()
    pygame.mixer_music.load("assets/space.ogg")
    pygame.mixer_music.set_volume(0.5)
    pygame.mixer_music.play(-1)

    destroyed_enemies = 0
    window = pygame.display.set_mode([800, 600])
    background_img = pygame.image.load("assets/galaxy.jpg")
    background_img = pygame.transform.scale(background_img, [800, 600])
    local_money = 0

    game_data = read_data()

    player = read_data()
    writing_data(player)

    fps = pygame.time.Clock()
    rocket = Rocket(400, 520, 5, player["skin"], 30, 70)
    meteors = [Meteor(225, 200), Meteor(400, 125)]

    enemies = []
    y = 50
    for i in range(10):
        x = random.randint(100, 700)
        enemies.append(Ufo(x, y, 3, 'assets/ufo.png', 60, 40))
        y -= 100

    running = True

    while running:
        window.blit(background_img, [0, 0])
        score = (pygame.font.Font(None, 50)
                 .render(f"Знищено: {str(destroyed_enemies)}", True, [255, 255, 255]))
        missed_enemies_lbl = (pygame.font.Font(None, 35)
                 .render(f"Пропущено: {str(missed_enemies)}", True, [255, 255, 255]))
        local_money_lbl = (pygame.font.Font(None, 35)
                              .render(f"Гроші: {str(local_money)}", True, [255, 255, 255]))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for meteor in meteors:
            meteor.draw(window)
        for enemy in enemies:
            enemy.draw(window)
            enemy.update()
        for bullet in rocket.bullets[:]:
            bullet.draw(window)
            bullet.update()
            for enemy in enemies:
                if bullet.hitbox.colliderect(enemy.hitbox):
                    rocket.bullets.remove(bullet)
                    enemy.hitbox.y = -100
                    enemy.hitbox.x = random.randint(100, 700)
                    destroyed_enemies += 1
                    money = read_data()
                    money["money"] += 1
                    writing_data(money)
                    local_money += 1
                    break
                elif bullet.hitbox.y <= game_data["range"]:
                    rocket.bullets.remove(bullet)
                    break
        window.blit(score, [0, 0])
        window.blit(missed_enemies_lbl, [0, 40])
        window.blit(local_money_lbl, [0, 70])
        rocket.draw(window)
        rocket.update()
        pygame.display.flip()
        fps.tick(60)

