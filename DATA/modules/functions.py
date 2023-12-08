from DATA.files.files.difficulties.easy import easy_init
from DATA.files.files.difficulties.normal import normal_init
from DATA.files.files.difficulties.hard import hard_init

from DATA.modules.base.button import Button
from DATA.modules.dice import Dice

from DATA.modules.variables import *
from datetime import datetime
import pygame
import json
import os


class Functions:
    #
    # playing menu buttons functions
    #

    @classmethod
    def func_play_buttons(cls, game, i):
        game.play_menu_buttons["activate"] = i if game.play_menu_buttons["activate"] != i else None

    @classmethod
    def func_play_menu_back(cls, game):
        game.play_menu_buttons["activate"] = None

    @classmethod
    def func_inventory_buttons(cls, game, i):
        game.play_inventory_buttons["active_button"] = i if game.play_inventory_buttons["active_button"] != i else None

    @classmethod
    def func_play_menu_quit_quit(cls, game):
        cls.play_quit(game)

        game.menu = "menu"

    @classmethod
    def func_play_menu_inventory_truns(cls, game):
        player = game.players.players[game.players.turn]
        number = game.play_inventory_buttons["active_button"]

        if number is None:
            return 0

        if number >= len(player.inventory):
            return 0

        if player.now == "attack":
            return 0

        if game.map.map[player.x][player.y]["name"] == "null":
            game.map.map[player.x][player.y] = game.cash["cells"][player.inventory[number]]

        else:
            player.add_item_inventory(player.x, player.y, True)
            game.map.map[player.x][player.y] = game.cash["cells"][player.inventory[number]]

        game.map.map[player.x][player.y]["visible"] = True

        player.inventory.pop(number)

        game.play_inventory_buttons["active_button"] = None

    @classmethod
    def func_play_menu_inventory_using(cls, game):
        player = game.players.players[game.players.turn]
        number = game.play_inventory_buttons["active_button"]

        if number is None:
            return 0

        if number >= len(player.inventory):
            return 0

        if game.cash["cells"][player.inventory[number]]["tag"].find("h") == -1:
            return 0

        player.health["now"] += min(player.health["max"], game.cash["cells"][player.inventory[number]]["add_health"])

        player.inventory.pop(number)
        player.add_item_inventory(player.x, player.y)

        game.play_inventory_buttons["active_button"] = None

    #
    # attack monster functions
    #

    @classmethod
    def func_button_attack_tnt(cls, game):
        player = game.players.players[game.players.turn]

        if "tnt" in player.inventory:
            game.players.players[game.players.turn].now = "go"

            game.map.map[player.x][player.y] = game.cash["cells"]["null"]

            for i in range(player.x - 1, player.x + 2):
                for j in range(player.y - 1, player.y + 2):
                    if 0 <= i <= 11 and 0 <= j <= 11:
                        if not game.map.map[i][j]["visible"]:
                            game.map.map[i][j]["visible"] = True

                            game.stats.money_for_game += GET_MONEY_FOR_OPEN_CELL

            game.players.next_tern()

            game.stats.money_for_game += GET_MONEY_FOR_KILL

            player.inventory.remove("tnt")

    @classmethod
    def func_button_live(cls, game):
        if game.cash["dices"]["live"] > BUTTON_LIVE:
            game.cash["dices"]["live"] = BUTTON_LIVE

    #
    # create play dices
    #

    @classmethod
    def create_go_dice(cls, game, get):
        game.cash["dices"] = {
            "draw": True,
            "button": Dice(
                game,
                200,
                200,
                200,
                200,
                (255, 255, 255),
                game.cash["sprites"]["dices"]["go"][str(get)],
                lambda: cls.func_button_live(game),
                "go"
            ),
            "live": 100000000000
        }

    @classmethod
    def create_attack_dice(cls, game, get):
        game.cash["dices"] = {
            "draw": True,
            "button": Dice(
                game,
                50,
                200,
                200,
                200,
                (255, 255, 255),
                game.cash["sprites"]["dices"]["attack"][str(get)],
                lambda: cls.func_button_live(game),
                "attack"
            ),
            "live": 100000000000
        }

        game.cash["button"] = {
            "draw": True,
            "button": Button(
                game,
                350,
                200,
                200,
                200,
                [
                    game.cash["sprites"]["dices"]["attack"]["null"],
                    game.cash["sprites"]["dices"]["attack"]["4"]
                ],
                lambda: cls.func_button_attack_tnt(game),
                (None, None, None)
            )
        }

    #
    # settings buttons
    #

    @classmethod
    def func_settings_menu(cls, game, unext):
        menues = [
            "auto",
            "summer",
            "autumn",
            "winter",
            "spring"
        ]

        if unext:
            for i, element in enumerate(menues):
                if element == game.settings["game_background"]:
                    game.settings["game_background"] = menues[(i + 1) % len(menues)]
                    break

            else:
                raise NameError("settings: game background not found")

        else:
            if game.settings["game_background"] == "auto":
                time = datetime.now()
                time = time.strftime("%m")

                game.couple = game.couples[time]

            else:
                game.couple = game.settings["game_background"]

        if unext:
            game.menu_settings_buttons["buttons"][0].text_box.text = translate.translate("Menu") + ": " + translate.translate(game.settings["game_background"])
            game.cash["settings_confirm"] = True

        return game.couple

    @classmethod
    def func_settings_font(cls, game):
        fonts = [
            "lucida",
            "arial"
        ]

        for i, element in enumerate(fonts):
            if element == game.settings["font"]:
                game.settings["font"] = fonts[(i + 1) % len(fonts)]
                break

        game.menu_settings_buttons["buttons"][1].text_box.text = translate.translate("Font") + ": " + translate.translate(game.settings["font"])
        game.cash["settings_confirm"] = True

    @classmethod
    def func_settings_lang(cls, game):
        langs = [
            "RU",
            "EN"
        ]

        for i, element in enumerate(langs):
            if element == game.settings["lang"]:
                game.settings["lang"] = langs[(i + 1) % len(langs)]
                break

        game.menu_settings_buttons["buttons"][2].text_box.text = translate.translate("Language") + ": " + cls.func_spec_translate_language(game.settings["lang"])
        game.cash["settings_confirm"] = True

    #
    # menu functions
    #

    @classmethod
    def func_menu_quit(cls, game):
        game.play = False

    @classmethod
    def func_menu_play(cls, game):
        cls.func_menu_back_append(game)

        game.menu = "choice_difficult"

    @classmethod
    def func_menu_history(cls, game):
        cls.func_menu_back_append(game)

        game.menu_history_buttons["text"][0].spec["auto_spawn_text"]["now"] = 0

        game.menu = "history"

    @classmethod
    def func_menu_help(cls, game):
        cls.func_menu_back_append(game)

        game.menu = "help"

    @classmethod
    def func_menu_settings(cls, game):
        cls.func_menu_back_append(game)

        game.menu = "settings"

    @classmethod
    def func_menu_stats(cls, game):
        cls.func_menu_back_append(game)

        game.menu = "stats"

    @classmethod
    def func_menu_shop(cls, game):
        cls.func_menu_back_append(game)

        game.menu = "shop"

    @classmethod
    def func_history_listen(cls, game):
        if game.sound.internet():
            game.sound.sound(game.cash["history"][LANG.lower()])

        else:
            print("bad connection.")

    #
    # menu back button
    #

    @classmethod
    def func_menu_back_append(cls, game):
        game.last_menu.append(game.menu)

    @classmethod
    def func_menu_back(cls, game):
        if len(game.last_menu) == 0:
            return 0

        game.menu = str(game.last_menu[-1])
        game.last_menu.pop(len(game.last_menu) - 1)

        pygame.mixer.stop()

        if game.cash["settings_confirm"]:
            cls.play_save(game)

            pygame.quit()

    #
    # choice game difficult
    #

    @classmethod
    def func_choice_easy(cls, game, players, map):
        game.cash["cells"] = easy_init(game)

        game.players = players(game)
        game.map = map(game)

        game.map.generate()

        game.play_inventory_buttons["active_button"] = None
        game.play_menu_buttons["activate"] = None

        game.menu = "play"

    @classmethod
    def func_choice_normal(cls, game, players, map):
        game.cash["cells"] = normal_init(game)

        game.players = players(game)
        game.map = map(game)

        game.map.generate()

        game.play_inventory_buttons["active_button"] = None
        game.play_menu_buttons["activate"] = None

        game.menu = "play"

    @classmethod
    def func_choice_hard(cls, game, players, map):
        game.cash["cells"] = hard_init(game)

        game.players = players(game)
        game.map = map(game)

        game.map.generate()

        game.play_inventory_buttons["active_button"] = None
        game.play_menu_buttons["activate"] = None

        game.menu = "play"

    #
    # leave for game
    #

    @classmethod
    def play_quit(cls, game):
        game.stats.money += game.stats.money_for_game
        game.stats.money_for_game = 0

        if game.map.game_complite:
            if game.stats.best_moves is not None:
                game.stats.best_moves = min(game.stats.moves, game.stats.best_moves)

            else:
                game.stats.best_moves = game.stats.moves

        game.menu = "menu"

    #
    # base settings
    #

    @classmethod
    def play_save(cls, game):
        path = "DATA/files/save/"

        with open(path + "game.json", "w") as file:
            json.dump({
                "money": game.stats.money,
                "best_moves": game.stats.best_moves
            }, file, indent=4)

        with open(path + "settings.json", "w") as file:
            json.dump(game.settings, file, indent=4)

    @classmethod
    def play_load(cls, game):
        path = "DATA/files/save/"

        if os.path.exists(path + "game.json"):
            try:
                with open(path + "game.json", "r") as file:
                    stats = json.load(file)

                game.stats.money = stats["money"]
                game.stats.best_moves = stats["best_moves"]

            except any:
                pass

        if os.path.exists(path + "settings.json"):
            with open(path + "settings.json", "r") as file:
                stats = json.load(file)

            game.settings = stats

        else:
            game.settings = {
                "game_background": "auto",
                "font": "lucida"
            }

    #
    # spec functions
    #

    @classmethod
    def func_spec_translate_language(cls, name):
        languages = {
            "RU": "Русский",
            "EN": "English"
        }

        return languages[name]
