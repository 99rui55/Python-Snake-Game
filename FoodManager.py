from GameSettings import GameSettings
import GraphicUtils
import random
from Food import Food


class FoodManager:
    def __init__(self, g_settings: GameSettings):
        self.g_settings = g_settings
        self.f_list = []

    def noFood(self):
        return len(self.f_list) == 0

    def generateFood(self):
        food_x = (
            random.randint(0, self.g_settings.g_width / self.g_settings.blockSize - 1)
            * self.g_settings.blockSize
        )
        food_y = (
            random.randint(
                0, (self.g_settings.g_height / self.g_settings.blockSize) - 1
            )
            * self.g_settings.blockSize
        )
        self.f_list.append(Food(self.g_settings, (food_x, food_y)))

    def removeFood(self, food: Food):
        self.f_list.remove(food)

    def drawFood(self):
        for f in self.f_list:
            if f.vis:
                GraphicUtils.DrawRectangle(
                    f.color,
                    (
                        f.position[0],
                        f.position[1],
                        self.g_settings.blockSize,
                        self.g_settings.blockSize,
                    ),
                )

    def blinkFood(self, time):
        for f in self.f_list:
            if time - f.last_vis_change > self.g_settings.f_blink_rate:
                f.ChangeVis()
                f.last_vis_change = time
