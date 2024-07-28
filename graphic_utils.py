import pygame
from game_settings import GameSettings
from snake import Snake

board = None


def DrawGrid(g_settings: GameSettings):
    """draw the snake game grid.

    Args:
        g_settings (GameSettings): the game settings object.
    """
    for i in range((g_settings.g_width // g_settings.blockSize) + 1):
        DrawRectangle(
            g_settings.g_color,
            (i * g_settings.blockSize, 0, g_settings.g_thickness, g_settings.g_height),
        )

    for i in range((g_settings.g_height // g_settings.blockSize) + 1):
        DrawRectangle(
            g_settings.g_color,
            (0, i * g_settings.blockSize, g_settings.g_width, g_settings.g_thickness),
        )


def DrawBoard(g_settings: GameSettings):
    """draw the board perimeter

    Args:
        g_settings (GameSettings): the game settings object.
    """
    DrawRectangle(
        g_settings.b_boarder_color,
        (0, 0, g_settings.b_width, 1),
    )
    DrawRectangle(
        g_settings.b_boarder_color,
        (0, 0, 1, g_settings.b_height),
    )
    DrawRectangle(
        g_settings.b_boarder_color,
        (0, g_settings.b_height, g_settings.b_width, 1),
    )
    DrawRectangle(
        g_settings.b_boarder_color,
        (g_settings.b_width, 0, 1, g_settings.b_height),
    )


def DrawSnake(g_settings: GameSettings, snake: Snake):
    """draw the snake

    Args:
        g_settings (GameSettings): the game settings object.
        snake (Snake): the snake object to draw.
    """
   
    for i in snake.snake:
        DrawRectangle(
            snake.color, (i[0], i[1], g_settings.blockSize, g_settings.blockSize)
        )


def DrawRectangle(color: tuple, position: tuple):
    """draw a rectangle to the screen

    Args:
        color (list): (R, G, B)
        position (list): (width, height, left top X, left top Y)
    """
    pygame.draw.rect(board, color, position)
