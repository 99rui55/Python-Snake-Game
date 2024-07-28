from GameSettings import GameSettings


class Food:
    def __init__(self, g_settings: GameSettings, position: list):
        self.g_settings = g_settings
        self.position = position
        self.last_vis_change = 0
        self.color = g_settings.f_color
        self.vis = True

    def changeVis(self):
        self.vis = not self.vis
