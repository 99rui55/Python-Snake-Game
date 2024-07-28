from game_settings import GameSettings


class Food:
    def __init__(self, g_settings: GameSettings, position: list):
        """constructor method for Food. 

        Args:
            g_settings (GameSettings): game settings
            position (list): [foodX, foodY]
        """
        self.g_settings = g_settings
        self.position = position
        self.last_vis_change = 0
        self.color = g_settings.f_color
        self.vis = True

    def ChangeVis(self):
        """change the visibility mode. 
        """
        self.vis = not self.vis
