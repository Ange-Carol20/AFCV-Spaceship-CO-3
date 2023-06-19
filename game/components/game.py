import pygame
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager

from game.components.enemies.enemy_manager import EnemyManager
from game.components.lose_menu import LoseMenu
from game.components.menu import Menu
from game.components.powerups.manager import Manager

from game.components.spaceship import Spaceship
from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0

        self.score = 0
        self.death_count = 0
        self.high_score = 0

        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.lose_menu = LoseMenu()
        self.menu = Menu("Press any key to start...")
        self.power_up_manager = Manager()

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                if self.death_count > 0:
                    self.show_lose_menu()
                else:
                    self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def play(self):
        self.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player_shoot() 

    def player_shoot(self):
        bullet = Bullet(self.player)
        self.bullet_manager.add_bullet(bullet)
        self.bullet_manager.player_bullets.append(bullet)

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        self.check_collision()
        
        if self.score > self.high_score:
            self.high_score = self.score

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

        if self.player.has_power_up:
            remaining_time = max(0, (self.player.power_up_time - pygame.time.get_ticks()) // 1000)
            power_up_text = font.render(f"Shield: {remaining_time}s", True, (255, 255, 255))
            power_up_text_rect = power_up_text.get_rect()
            power_up_text_rect.center = (1000, 80)
            self.screen.blit(power_up_text, power_up_text_rect)

    def show_menu(self):
        self.menu.draw(self.screen)
        self.menu.event(self.on_close, self.play)

    def show_lose_menu(self):
        self.lose_menu.update_score(self.score)
        self.lose_menu.update_high_score(self.high_score)
        self.lose_menu.update_death_count(self.death_count)
        self.lose_menu.draw(self.screen)
        self.lose_menu.event(self.on_close, self.play)

    def on_close(self):
        self.playing = False
        self.running = False
    
    def reset(self):
        self.enemy_manager.reset()
        self.playing = True
        self.score = 0
        self.power_up_manager.reset()

    def check_collision(self):
        if not self.player.has_power_up:  # verificar si el jugador tiene el escudo activado
            if pygame.sprite.spritecollideany(self.player, self.enemy_manager.enemies):
                self.playing = False
                pygame.time.delay(1000)
        
