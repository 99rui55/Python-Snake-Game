from GameSettings import GameSettings


class Snake:
    def __init__(self, g_settings: GameSettings, color=(255, 255, 255), initPos=(0, 0)):
        self.color = color
        self.snake = []
        self.snake.append(initPos)
        self.g_settings = g_settings
        self.s_length = 1
        self.direction = (0, 1)
        self.last_direction = self.direction
        self.head = initPos
        self.last_moved = 0

    def setDirection(self, direction: list):
        self.direction = direction

    def move(self):
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

    def isDead(self) -> bool:
        for i in range(len(self.snake) - 2):
            if self.head[0] == self.snake[i][0] and self.head[1] == self.snake[i][1]:
                return True
        return False

    def checkFoodContact(self, f_list: list) -> list:
        for f in f_list:
            if self.head[0] == f.position[0] and self.head[1] == f.position[1]:
                return f

    def addToSnake(self, length):
        self.s_length += length
        if self.s_length % 3 == 0:
            self.g_settings.s_speed += 1

    def restart(self):
        self.snake = []
        self.snake.append((0, 0))
        self.s_length = 1
        self.direction = (0, 1)
        self.last_direction = self.direction
        self.head = (0, 0)
        self.last_moved = 0
