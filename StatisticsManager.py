import pygame
import GraphicUtils
from Snake import Snake
from GameSettings import GameSettings


class StatisticsManager:
    def __init__(self, g_settings: GameSettings, snake: Snake, board):
        self.g_settings = g_settings
        self.snake = snake
        self.board = board

    def Update(self, g_settings, snake):
        self.g_settings = g_settings
        self.snake = snake

    def DrawStatistics(self):
        font = pygame.font.Font("freesansbold.ttf", 32)
        score = self.snake.s_length
        speed = self.g_settings.s_speed

        t_score = font.render(f"Score: {score}", True, (255, 255, 255), (0, 0, 0))
        tr_score = t_score.get_rect()
        tr_score.topleft = (self.g_settings.g_width + 10, 20)

        t_speed = font.render(f"Speed: {speed}", True, (255, 255, 255), (0, 0, 0))
        tr_speed = t_speed.get_rect()
        tr_speed.topleft = (self.g_settings.g_width + 10, 80)

        self.board.blit(t_score, tr_score)
        self.board.blit(t_speed, tr_speed)

    def DisplayEndMessage(self):
        font = pygame.font.Font("freesansbold.ttf", 32)
        t_end = font.render(
            "Game Has Ended! to play again, press A. to exit, press E",
            True,
            (255, 255, 255),
            (0, 0, 0),
        )
        tr_end = t_end.get_rect()
        tr_end.topleft = (20, 150)

        self.board.blit(t_end, tr_end)
