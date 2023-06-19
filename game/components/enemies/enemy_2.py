import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy2(Enemy):
    SPEED_X = 5
    SPEED_Y = 1

    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS    
        self.type = ENEMY_TYPE

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

        self.move_x = random.randint(30, 100)
        self.moving_index = 0
        self.zigzag_counter = 0
        self.shooting_time = random.randint(40, 60)

    def update(self, ships, game):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)

        self.update_movement()
        if self.rect.y >= SCREEN_HEIGHT or self.rect.x >= SCREEN_WIDTH:
            ships.remove(self)
    
    def update_movement(self):
        if self.rect.x >= SCREEN_WIDTH - 50 or self.rect.x <= 0:
            self.speed_x = -self.speed_x
        if self.rect.y >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y