from DATA.modules.variables import *

from PIL import ImageFont
import pygame


class TextField:
    """
    spec = {
        "scroll": {
            "add": int
        },

        "auto_spawn_text": {
            "step": int,
            "now": int
        }
    }

    """

    def __init__(self, game, x, y, width, height, text, font_size=20,
                 font_type=BASE_FONT, font_color=FRAME_COLOR, spec=None):

        if spec is None:
            self.spec = {}
        else:
            self.spec = spec

        self.game = game

        self.x = x
        self.y = y

        self.text = text

        self.font_size = font_size
        self.font_type = font_type
        self.font_color = font_color

        self.ttf = ImageFont.truetype(self.font_type, self.font_size)

        self.width = width
        self.height = height

        self.out = []

        var = 0
        st = 0

        self.hstep = self.ttf.getbbox("Ag")[3]

        self.text = self.text.split()

        if len(self.text) != 0:
            i = 0

            self.out.append([])

            for i, word in enumerate(self.text):
                var = self.ttf.getbbox(word)[2]

                if var + self.ttf.getbbox(" ".join(self.out[len(self.out) - 1]) + (i - st + 1) * " ")[2] < self.width:
                    if word == "/n":
                        st = i
                        self.out.append([])

                    elif word == "/t":
                        self.out[len(self.out) - 1].append("    ")

                    else:
                        self.out[len(self.out) - 1].append(word)

                else:
                    if word == "/n":
                        st = i
                        self.out.append([])

                    elif word == "/t":
                        self.out[len(self.out) - 1].append("    ")

                    else:
                        self.out[len(self.out) - 1].append(word)

                    st = i
                    self.out.append([])

    def draw(self, x=None, y=None):
        if x is None:
            x = self.x

        if y is None:
            y = self.y

        if self.spec.get("auto_spawn_text") is not None:
            self.spec["auto_spawn_text"]["now"] += self.spec["auto_spawn_text"]["step"]

        font = pygame.font.Font(self.font_type, self.font_size)

        if self.spec.get("scroll") is not None:
            add = self.spec["scroll"]["add"]

        else:
            add = 0

        if self.spec.get("auto_spawn_text") is not None:
            step = self.spec["auto_spawn_text"]["now"]

        else:
            step = 10000000000000000000

        now = 0
        for i, element in enumerate(self.out):
            if now + len(" ".join(element)) > step:
                if self.hstep * (i - add) <= self.height and i - add >= 0:
                    text = font.render(" ".join(element)[:round(step - now)], True, self.font_color)
                    self.game.screen.blit(text, (x, y + self.hstep * (i - add)))

                return 0

            else:
                if self.hstep * (i - add) <= self.height and i - add >= 0:
                    text = font.render(" ".join(element), True, self.font_color)
                    self.game.screen.blit(text, (x, y + self.hstep * (i - add)))

            now += len(" ".join(element))
