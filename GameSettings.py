class GameSettings:
    # w_for window, b_ for board, g_ for grid, s_ for snake
    def __init__(
        self,
        w_width,
        w_height,
        b_width,
        b_height,
        b_color,
        b_boarder_color,
        blockSize,
        g_thickness,
        g_color,
        f_blink_rate,
        f_color,
        s_speed,
    ):
        self.w_width = w_width
        self.w_height = w_height
        self.b_width = b_width
        self.b_height = b_height
        self.b_color = b_color
        self.b_boarder_color = b_boarder_color
        self.blockSize = blockSize
        self.g_thickness = g_thickness
        self.g_color = g_color
        self.g_width = b_width - b_width % blockSize
        self.g_height = b_height - b_height % blockSize
        self.f_blink_rate = f_blink_rate
        self.f_color = f_color
        self.s_speed = s_speed

    def restart(self):
        self.s_speed = 8


game_settings = GameSettings(
    w_width=1000,
    w_height=750,
    b_width=750,
    b_height=500,
    b_color=(0, 0, 0),
    b_boarder_color=(255, 255, 255),
    blockSize=30,
    g_thickness=2,
    g_color=(0, 6, 184),
    f_blink_rate=500,
    f_color=(255, 255, 255),
    s_speed=8,
)
