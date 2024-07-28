from game_settings import GameSettings
from food import Food

class Snake:
    def __init__(self, g_settings: GameSettings, color=(255, 255, 255), initPos=(0, 0)):
        """Snake object constructor

        Args:
            g_settings (GameSettings): game settings object.
            color (tuple, optional): color of snake. Defaults to (255, 255, 255).
            initPos (tuple, optional): initial position of snake. Defaults to (0, 0).
        """
        self.color = color
        self.snake = []
        self.snake.append(initPos)
        self.g_settings = g_settings
        self.s_length = 1
        self.direction = (0, 0)
        self.last_direction = self.direction
        self.head = initPos
        self.last_moved = 0

    def SetDirection(self, direction: tuple):
        """set the movement direction of the snake

        Args:
            direction (list): a [x,y] unit vector of the movement
        """
        self.direction = direction

    def Move(self):
        """calculate and update the snake
        """
        new_head_x = (
            self.head[0] + self.direction[0] * self.g_settings.blockSize
        ) % self.g_settings.g_width
        new_head_y = (
            self.head[1] + self.direction[1] * self.g_settings.blockSize
        ) % self.g_settings.g_height

        self.snake.append((new_head_x, new_head_y))
        self.head = (new_head_x, new_head_y)
        if len(self.snake) > self.s_length:
            self.snake.pop(0)

        self.last_direction = self.direction

    def IsDead(self) -> bool:
        """checks if snake is coliding with himself

        Returns:
            bool: True if snake colided with itself.
        """
        for i in range(len(self.snake) - 2):
            if self.head[0] == self.snake[i][0] and self.head[1] == self.snake[i][1]:
                return True
        return False

    def CheckFoodContact(self, f_list: list) -> Food:
        """checks if snake is touching food

        Args:
            f_list (list): a list of Food

        Returns:
            Food: a food object that came in contact with the snake head. if none, returns None.
        """
        for f in f_list:
            if self.head[0] == f.position[0] and self.head[1] == f.position[1]:
                return f

    def AddToSnake(self, length: int):
        """add length to snake

        Args:
            length (int): the length to be added
        """
        self.s_length += length
        if self.s_length % 3 == 0:
            self.g_settings.s_speed += 1

    def Restart(self):
        """restart snake.
        """
        self.snake = []
        self.snake.append((0, 0))
        self.s_length = 1
        self.direction = (0, 0)
        self.last_direction = self.direction
        self.head = (0, 0)
        self.last_moved = 0
