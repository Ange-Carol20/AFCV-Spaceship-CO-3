import pygame
from game.components.menu import Menu
from game.utils.constants import FONT_STYLE, GAMEOVER


class LoseMenu(Menu):

    def __init__(self, text_size=25):
        self.font = pygame.font.Font(FONT_STYLE, text_size)
        self.icon = pygame.transform.scale(GAMEOVER, (600, 550))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        self.score_text = 0
        self.high_score_text = 0
        self.death_count_text = 0
        self.update_message("Press any key to restart")

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
        screen.blit(self.icon, self.icon_rect)
        screen.blit(self.score_text, self.score_text_rect)
        screen.blit(self.high_score_text, self.high_score_text_rect)
        screen.blit(self.death_count_text, self.death_count_text_rect)
        pygame.display.update()

    def update_score(self, score):
        self.score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)

    def update_high_score(self, high_score):
        self.high_score_text = self.font.render(f"High Score: {high_score}", True, (255, 255, 255))
        self.high_score_text_rect = self.high_score_text.get_rect()
        self.high_score_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)

    def update_death_count(self, death_count):
        self.death_count_text = self.font.render(f"Death Count: {death_count}", True, (255, 255, 255))
        self.death_count_text_rect = self.death_count_text.get_rect()
        self.death_count_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)