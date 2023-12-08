from DATA.files.files.difficulties.easy import easy_init

import pygame


def init(game):
    """
    s - spawn
    e - enemy
    g - get
    h - health
    """

    path = "DATA/files/sprites/"

    game.cash["settings_confirm"] = False

    game.cash["dices"] = {
        "draw": False,
        "button": None,
        "live": 0
    }

    game.cash["button"] = {
        "draw": False,
        "button": None
    }

    game.cash["history"] = {
        "ru": """
            /t Космонавты искали новую планету так как земля стала непригодной для жизни. Они очень долго исследовали космос, топливо и еда должна была закончиться через 30 дней, а новых планет не было на радаре.
            /n /t И вдруг они обнаружили, что в 100000 км от корабля, есть планета схожая с землёй так как им могло не хватить топлива и еды, путешествовать дальше по космосу они решили исследовать эту планету, в надежде что им больше не придётся бороздить по космосу. Космонавты поставили ориентир на эту планету и им пришлось ждать 25 дней чтобы добраться до этой планет и за это время они даже не готовились к тому, что на планете могут обитать опасные существа. Когда они добрались до планеты и преодолели атмосферу в их корабль попал снаряд и корабль начал падать. Космонавтам пришлось катапультироваться чтобы не разбиться. Корабль упал где-то на неизведанной планете, а космонавты приземлились полным составом на неизведанную планету.
            /n /t Теперь главной их задачей будет не исследование планеты, а поиск корабля так как планета оказалась заселена агрессивно настроенными пришельцами. Так как у корабля осталось мало топлива надо найти замену ему или синтезировать его из инопланетных ресурсов, а также от корабля отлетела деталь, без которой корабль не взлетит, которую тоже нужно отыскать. Ну и конечно же надо найти сам корабль. И только тогда, когда ребята найдут корабль, починят его и улетят с этой планеты игра будет считаться пройденной… А пока что вас ждёт увлекательное путешествие по не изведанной планете, сбор ресурсов, поиск корабля, сражения с пришельцами и многое другое. В игре вы научитесь работать в команде, помогать друг другу, также вы можете продумывать, как лучше поступать в сложных ситуациях, как распоряжаться своими ресурсами и многое другое.
            /n /t Помни, когда мы едины мы непобедимы.

        """,

        "en": """
            /t The astronauts were looking for a new planet because the earth had become uninhabitable. They explored space for a very long time, fuel and food were supposed to run out in 30 days, and there were no new planets on the radar.
            /n /t And suddenly they discovered that 100,000 km from the ship, there is a planet similar to the earth. Since they might not have enough fuel and food, they decided to travel further through space to explore this planet, in the hope that they would no longer have to roam through space. The astronauts set a landmark on this planet and they had to wait 25 days to get to this planet, and during this time they did not even prepare for the fact that dangerous creatures could live on the planet. When they reached the planet and overcame the atmosphere, a shell hit their ship and the ship began to fall. The astronauts had to eject to avoid crashing. The ship crashed somewhere on an uncharted planet, and the astronauts landed in full force on an uncharted planet.
            /n /t Now their main task will not be to explore the planet, but to search for a ship, since the planet turned out to be inhabited by aggressive aliens. Since the ship has little fuel left, it is necessary to find a replacement for it or synthesize it from alien resources, and a part has flown off the ship, without which the ship will not take off, which also needs to be found. And of course, you need to find the ship itself. And only when the guys find the ship, fix it and fly away from this planet will the game be considered completed... In the meantime, an exciting journey through an unexplored planet awaits you, collecting resources, searching for a ship, fighting aliens and much more. In the game you will learn to work in a team, help each other, you can also think about how best to act in difficult situations, how to manage your resources and much more.
            /n /t Remember, when we are united we are invincible.
        """
    }

    game.cash["menues"] = {
        "winter": {
            "bg": pygame.image.load(path + "menues/winter/bg.jpg").convert_alpha(game.screen),
            "mouse": pygame.image.load(path + "menues/winter/mouse.png").convert_alpha(game.screen),

            "button_color": [(200, 200, 240, 20), (200, 200, 240, 60), (200, 200, 240)],
            "font_color": (200, 200, 240),
            "snow_color": (180, 180, 220)
        },

        "summer": {
            "bg": pygame.image.load(path + "menues/summer/bg.jpg").convert_alpha(game.screen),
            "mouse": pygame.image.load(path + "menues/summer/mouse.png").convert_alpha(game.screen),

            "button_color": [(170, 180, 130, 20), (170, 180, 130, 60), (170, 180, 130)],
            "font_color": (170, 180, 130, 110 + 20),
        },

        "autumn": {
            "bg": pygame.image.load(path + "menues/autumn/bg.jpg").convert_alpha(game.screen),
            "mouse": pygame.image.load(path + "menues/autumn/mouse.png").convert_alpha(game.screen),

            "button_color": [(220, 130, 80, 20), (220, 130, 80, 60), (220, 130, 80)],
            "font_color": (220, 130, 80),
        },

        "spring": {
            "bg": pygame.image.load(path + "menues/spring/bg.jpg").convert_alpha(game.screen),
            "mouse": pygame.image.load(path + "menues/spring/mouse.png").convert_alpha(game.screen),

            "button_color": [(170, 180, 130, 20), (170, 180, 130, 60), (170, 180, 130)],
            "font_color": (170, 180, 130),
        }
    }

    game.cash["sprites"] = {
        "map": pygame.transform.scale(pygame.image.load(path + "map.png").convert_alpha(game.screen), (1000, 1000)),
        "step": pygame.image.load(path + "step.png").convert_alpha(game.screen),
        "mouse": pygame.image.load(path + "mouse.png").convert_alpha(game.screen),

        "died": pygame.image.load(path + "died.png").convert_alpha(game.screen),

        "ship": {
            "1": pygame.image.load(path + "cells/ship_bar_1.png").convert_alpha(game.screen),
            "2": pygame.image.load(path + "cells/ship_bar_2.png").convert_alpha(game.screen),
            "3": pygame.image.load(path + "cells/ship_bar_3.png").convert_alpha(game.screen)
        },

        "actions": {
            "1": pygame.image.load(path + "actions/1.png").convert_alpha(game.screen),
            "2": pygame.image.load(path + "actions/2.png").convert_alpha(game.screen),
            "3": pygame.image.load(path + "actions/3.png").convert_alpha(game.screen),
            "4": pygame.image.load(path + "actions/4.png").convert_alpha(game.screen)
        },

        "fields": {
            "4_1": pygame.image.load(path + "fields/4_1.png").convert_alpha(game.screen),
            "4_4": pygame.image.load(path + "fields/4_4.png").convert_alpha(game.screen)
        },

        "menu_button": {
            "1": pygame.image.load(path + "menu_button.png").convert_alpha(game.screen)
        },

        "dices": {
            "go": {
                "0": pygame.image.load(path + "dices/go/0.png").convert_alpha(game.screen),
                "1": pygame.image.load(path + "dices/go/1.png").convert_alpha(game.screen),
                "2": pygame.image.load(path + "dices/go/2.png").convert_alpha(game.screen),
                "3": pygame.image.load(path + "dices/go/3.png").convert_alpha(game.screen),
                "4": pygame.image.load(path + "dices/go/4.png").convert_alpha(game.screen),
                "5": pygame.image.load(path + "dices/go/5.png").convert_alpha(game.screen),
                "6": pygame.image.load(path + "dices/go/6.png").convert_alpha(game.screen),

                "null": pygame.image.load(path + "dices/go/null.png").convert_alpha(game.screen),
            },

            "attack": {
                "0": pygame.image.load(path + "dices/attack/0.png").convert_alpha(game.screen),
                "1": pygame.image.load(path + "dices/attack/1.png").convert_alpha(game.screen),
                "2": pygame.image.load(path + "dices/attack/2.png").convert_alpha(game.screen),
                "3": pygame.image.load(path + "dices/attack/3.png").convert_alpha(game.screen),
                "4": pygame.image.load(path + "dices/attack/4.png").convert_alpha(game.screen),

                "null": pygame.image.load(path + "dices/attack/null.png").convert_alpha(game.screen),
            }
        },

        "player": {
            "health": [
                pygame.image.load(path + "health/health.png").convert_alpha(game.screen),
                pygame.image.load(path + "health/empty_health.png").convert_alpha(game.screen)
            ]
        },

        "cells": {
            "null": pygame.image.load(path + "cells/null.png").convert_alpha(game.screen),
            "enemy_1": pygame.image.load(path + "cells/enemy_1.png").convert_alpha(game.screen),
            "enemy_2": pygame.image.load(path + "cells/enemy_2.png").convert_alpha(game.screen),
            "enemy_3": pygame.image.load(path + "cells/enemy_3.png").convert_alpha(game.screen),
            "tnt": pygame.image.load(path + "cells/tnt.png").convert_alpha(game.screen),
            "gun_1": pygame.image.load(path + "guns/1.png").convert_alpha(game.screen),
            "gun_2": pygame.image.load(path + "guns/2.png").convert_alpha(game.screen),
            "gun_3": pygame.image.load(path + "guns/3.png").convert_alpha(game.screen),
            "gun_4": pygame.image.load(path + "guns/4.png").convert_alpha(game.screen),
            "gun_5": pygame.image.load(path + "guns/5.png").convert_alpha(game.screen),
            "health_add_1": pygame.image.load(path + "cells/health_add_1.png").convert_alpha(game.screen),
            "health_add_3": pygame.image.load(path + "cells/health_add_3.png").convert_alpha(game.screen),
            "fuel": pygame.image.load(path + "cells/fuel.png").convert_alpha(game.screen),
            "detail": pygame.image.load(path + "cells/detail.png").convert_alpha(game.screen),
            "ship": pygame.image.load(path + "cells/ship.png").convert_alpha(game.screen),
            "not_open": pygame.image.load(path + "cells/not_open.png").convert_alpha(game.screen)
        }
    }

    game.cash["cells"] = easy_init(game)
