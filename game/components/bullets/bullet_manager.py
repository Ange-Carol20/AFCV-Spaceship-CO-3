import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE


class BulletManager:
    def __init__(self):
        #self.bullets = list[Bullet] = []
        self.player_bullets = []
        self.enemy_bullets: list[Bullet] = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            #Verificar si hemos chocado con el jugador
            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(bullet)
                game.playing = False
                game.death_count += 1
                pygame.time.delay(1000)
                break

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            # Verificar si hemos golpeado a un enemigo
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    game.enemy_manager.enemies.remove(enemy)
                    game.score += 1
                    self.player_bullets.remove(bullet)
                    

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)