import pygame
from GameSettings import GameSettings
from Snake import Snake

board = None


def drawGrid(g_settings: GameSettings):
    for i in range((g_settings.g_width // g_settings.blockSize) + 1):
        drawRectangle(
            g_settings.g_color,
            (i * g_settings.blockSize, 0, g_settings.g_thickness, g_settings.g_height),
        )

    for i in range((g_settings.g_height // g_settings.blockSize) + 1):
        drawRectangle(
            g_settings.g_color,
            (0, i * g_settings.blockSize, g_settings.g_width, g_settings.g_thickness),
        )


def drawBoard(g_settings: GameSettings):
    drawRectangle(
        g_settings.b_boarder_color,
        (0, 0, g_settings.b_width, 1),
    )
    drawRectangle(
        g_settings.b_boarder_color,
        (0, 0, 1, g_settings.b_height),
    )
    drawRectangle(
        g_settings.b_boarder_color,
        (0, g_settings.b_height, g_settings.b_width, 1),
    )
    drawRectangle(
        g_settings.b_boarder_color,
        (g_settings.b_width, 0, 1, g_settings.b_height),
    )


def drawSnake(g_settings: GameSettings, snake: Snake):
    for i in snake.snake:
        drawRectangle(
            snake.color, (i[0], i[1], g_settings.blockSize, g_settings.blockSize)
        )


def drawRectangle(color: list, position: list):
    pygame.draw.rect(board, color, position)
