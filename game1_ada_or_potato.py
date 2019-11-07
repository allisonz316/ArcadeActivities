import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Ada or Potato"
GAME_SPEED = 1/60

TIMER_MAXIMUM = 100


NEXT_PHASE = {
    'ada': 'potato',
    'potato': 'ada',
    }


class Ada(arcade.Sprite):
    phase: str
    timer: int

    def __init__(self):
        super().__init__("images/ada.png")
        self.phase = 'ada'
        self.timer = 0
        self.center_x = WINDOW_WIDTH/2
        self.center_y = WINDOW_HEIGHT/2

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0
            self.phase = NEXT_PHASE[self.phase]

    def hide(self):
        if self.phase == "potato":
            self.center_x = 1000
            self.center_y = 1000
        elif self.phase == "ada":
            self.center_x = WINDOW_WIDTH / 2
            self.center_y = WINDOW_HEIGHT / 2

    def update(self):
        self.update_timer()
        self.hide()


class Potato(arcade.Sprite):
    phase: str
    timer: int

    def __init__(self):
        super().__init__("images/potato.png")
        self.phase = 'ada'
        self.timer = 0
        self.center_x = 1000
        self.center_y = 1000
        self.height = 500
        self.width = 300

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0
            self.phase = NEXT_PHASE[self.phase]

    def hide(self):
        if self.phase == "potato":
            self.center_x = WINDOW_WIDTH / 2
            self.center_y = WINDOW_HEIGHT / 2
        elif self.phase == "ada":
            self.center_x = 1000
            self.center_y = 1000

    def update(self):
        self.update_timer()
        self.hide()


class AdaOrPotatoGame(arcade.Window):
    points = 0

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.pic_list = None

    def setup(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        self.pic_list = arcade.SpriteList()
        self.pic_list.append(Ada())
        self.pic_list.append(Potato())

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.pic_list.draw()

    def on_update(self, delta_time):
        self.pic_list.update()


def main():
    window = AdaOrPotatoGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
