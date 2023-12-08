from DATA.modules.base.print_text import print_text
from DATA.modules.base.alpha_rect import alpha_rect
from DATA.modules.base.text_box import TextBox

from DATA.modules.variables import *
import pygame
import random


class Render:
    def __init__(self, game):
        self.game = game

    def play(self):
        if self.game.debug["draw_map"]:
            self.game.screen.blit(self.game.cash["sprites"]["map"], (-200, -200))

        alpha_rect(self.game.screen, WIDTH, HEIGHT, 0, 0, (0, 120, 0, 5))

        pygame.draw.rect(self.game.screen, BG_COLOR, (600, 0, 600, HEIGHT))

        for i in range(self.game.map.height):
            for j in range(self.game.map.width):
                if self.game.map.map[j][i]["visible"]:
                    if self.game.map.map[j][i]["name"] != "null" and self.game.map.map[j][i]["sprite"] is not None:
                        self.game.screen.blit(self.game.map.map[j][i]["sprite"], (j * CELLSIZE, i * CELLSIZE))

                    if self.game.map.map[j][i]["name"] == "ship" and self.game.map.ship_complite != 0:
                        self.game.screen.blit(self.game.cash["sprites"]["ship"][str(self.game.map.ship_complite)], (j * CELLSIZE + 1, i * CELLSIZE))

                else:
                    pygame.draw.rect(self.game.screen, FRAME_COLOR, (j * CELLSIZE, i * CELLSIZE, CELLSIZE, CELLSIZE))

        if self.game.debug["cells"]:
            for i in range(self.game.map.height):
                for j in range(self.game.map.width):
                    pygame.draw.rect(self.game.screen, BG_COLOR, (j * CELLSIZE, i * CELLSIZE, CELLSIZE, CELLSIZE), 1)

        self.game.players.draw()

        if self.game.cash["dices"]["draw"]:
            self.game.cash["dices"]["button"].draw()

        if self.game.cash["button"]["draw"]:
            self.game.cash["button"]["button"].draw()

        if self.game.play_menu_buttons["activate"] is not None:
            self.game.play_menu_buttons["back"].draw()

            pygame.draw.rect(self.game.screen, BG_COLOR, (603, 453, 361, 146))

            player = self.game.players.players[self.game.players.turn]

            if self.game.play_menu_buttons["activate"] == 0:
                for button in self.game.play_inventory_buttons["buttons"]:
                    button.draw()

                for button in self.game.play_inventory_buttons["use_buttons"]:
                    button.draw()

                print_text(self.game.screen, 702, 451, player.name, 20, font_color=AV_COLOR)
                pygame.draw.rect(self.game.screen, AV_COLOR, (603, 453, 96, 96))
                self.game.screen.blit(player.sprite[1], (602, 452))

                for j, item in enumerate(player.inventory):
                    self.game.screen.blit(self.game.cash["cells"][item]["sprite"], (702 + j * 53, 499))

                if self.game.play_inventory_buttons["active_button"] is not None:
                    alpha_rect(self.game.screen, 50, 50, 702 + self.game.play_inventory_buttons["active_button"] * 53, 499, (80, 125, 181, 100))

            if self.game.play_menu_buttons["activate"] == 1:
                pass

            if self.game.play_menu_buttons["activate"] == 2:
                for text in self.game.play_stats_buttons["text"]:
                    text.draw()

            if self.game.play_menu_buttons["activate"] == 3:
                for button in self.game.play_quit_buttons["buttons"]:
                    button.draw()

        else:
            for button in self.game.play_menu_buttons["buttons"]:
                button.draw()

        pygame.draw.rect(self.game.screen, AV_COLOR, (967, 3, 32, 596))

    def menu(self):
        self.draw_background()

        for button in self.game.menu_menu_buttons["buttons"]:
            button.draw()

        for text in self.game.menu_menu_buttons["text"]:
            text.draw()

    def choice_difficult(self):
        self.draw_background()

        for button in self.game.menu_choice_buttons["buttons"]:
            button.draw()

        for text in self.game.menu_choice_buttons["text"]:
            text.draw()

        self.game.menu_back_button.draw()

    def stats(self):
        self.draw_background()

        font_color = self.game.cash["menues"][self.game.couple]["font_color"]

        if self.game.stats.best_moves is not None:
            TextBox(self.game, 5, 0, WIDTH, 25, translate.translate("Minimum number of moves") + ": " + str(self.game.stats.best_moves), type="left", font_color=font_color).draw()
        else:
            TextBox(self.game, 5, 0, WIDTH, 25, translate.translate("Minimum number of moves") + ": " + translate.translate("indefinably"), type="left", font_color=font_color).draw()

        self.game.menu_back_button.draw()

    def help(self):
        self.draw_background()

        for button in self.game.menu_help_buttons["buttons"]:
            button.draw()

        for text in self.game.menu_help_buttons["text"]:
            text.draw()

        self.game.menu_back_button.draw()

    def shop(self):
        self.draw_background()

        for text in self.game.menu_shop_buttons["text"]:
            text.draw()

        self.game.menu_back_button.draw()

    def history(self):
        self.draw_background()

        for button in self.game.menu_history_buttons["buttons"]:
            button.draw()

        for text in self.game.menu_history_buttons["text"]:
            text.draw()

    def settings(self):
        self.draw_background()

        for button in self.game.menu_settings_buttons["buttons"]:
            button.draw()

        if self.game.cash["settings_confirm"]:
            print_text(self.game.screen, 205, 568, translate.translate("Request restarting!"), 30, font_color=self.game.cash["menues"][self.game.couple]["font_color"])

        self.game.menu_back_button.draw()

    def draw_background(self):
        self.game.screen.blit(self.game.cash["menues"][self.game.couple]["bg"], (0, 0))
        self.draw_menu()

        # pygame.draw.rect(self.game.screen, (255, 0, 0), (200, 0, 600, 600), 1)

        if self.game.debug["particles"]:
            if self.game.couple == "winter":
                self.game.particles.create(
                    random.randint(0, 1400), random.randint(-100, 0),
                    self.game.cash["menues"][self.game.couple]["snow_color"],
                    90, 8, random.randint(5, 7), 0.035
                )

    def draw_menu(self):
        alpha_rect(self.game.screen, WIDTH, HEIGHT, 0, 0, (0, 0, 0, 50))

    def render(self):
        self.game.screen.fill(BG_COLOR)

        if self.game.debug["fps"]:
            pygame.display.set_caption(str(round(self.game.clock.get_fps(), 1)))

        if self.game.menu == "play":
            self.play()

        if self.game.menu == "menu":
            self.menu()

        if self.game.menu == "help":
            self.help()

        if self.game.menu == "shop":
            self.shop()

        if self.game.menu == "stats":
            self.stats()

        if self.game.menu == "history":
            self.history()

        if self.game.menu == "settings":
            self.settings()

        if self.game.menu == "choice_difficult":
            self.choice_difficult()

        if all([self.game.mouse[0] != 0, self.game.mouse[1] != 0]):
            if self.game.menu == "play":
                self.game.screen.blit(self.game.cash["sprites"]["mouse"], (self.game.mouse[0], self.game.mouse[1]))

            else:
                self.game.screen.blit(self.game.cash["menues"][self.game.couple]["mouse"], (self.game.mouse[0], self.game.mouse[1]))

        self.game.particles.draw()

        pygame.display.update()
