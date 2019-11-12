import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Ada or Potato"
GAME_SPEED = 1/60

TIMER_MAXIMUM = 50

IMAGE_ADA = arcade.load_texture("images/ada.png")
IMAGE_POTATO = arcade.load_texture("images/potato.png", 1180, 872.5, 281, 444)


class AdaOrPotato(arcade.Sprite):
    timer: int

    def __init__(self):
        super().__init__()
        self.phase = 'ada'
        self.timer = 0
        self.center_x = WINDOW_WIDTH/2
        self.center_y = WINDOW_HEIGHT/2
        self.width = 281
        self.height = 444
        self.texture = IMAGE_ADA
        self.points = 0

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0
            self.switch_image()

    def switch_image(self):
        if self.texture == IMAGE_ADA:
            self.texture = IMAGE_POTATO
        else:
            self.texture = IMAGE_ADA

    def update(self):
        self.update_timer()


class AdaOrPotatoGame(arcade.Window):
    points = 0

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.pic_list = None

    def setup(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        self.pic_list = arcade.SpriteList()
        self.pic_list.append(AdaOrPotato())

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.pic_list.draw()
        arcade.draw_text(f"Points: {self.points}", 20, 50, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        self.pic_list.update()
        arcade.draw_text(f"Points: {self.points}", 20, 50, arcade.color.WHITE, 14)

    def on_mouse_press(self, x, y, button, modifiers):
        for pic in self.pic_list:
            if pic.texture == IMAGE_ADA:
                self.points = self.points + 1
            elif pic.texture == IMAGE_POTATO:
                self.points = self.points - 2


def main():
    window = AdaOrPotatoGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
