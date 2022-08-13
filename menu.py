import pygame
import pygame_menu

import game
from Players.AI.algorithm import Algorithm
from ingame_properties import Properties


COLOR_BACKGROUND = (153, 153, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60
MENU_BACKGROUND_COLOR = (102, 102, 153)
MENU_TITLE_COLOR = (51, 51, 255)

pygame.display.init()
INFO = pygame.display.Info()
TILE_SIZE = int(INFO.current_h * 0.035)
WINDOW_SIZE = (13 * TILE_SIZE, 13 * TILE_SIZE)

clock = None
surface = pygame.display.set_mode(WINDOW_SIZE)


properties = Properties()


def change_path(value, c):
    properties.set_pathing(c)


def change_player(value, c):
    properties.set_algorithm(1, c)


def change_enemy1(value, c):
    properties.set_algorithm(2, c)


def change_enemy2(value, c):
    properties.set_algorithm(3, c)


def change_enemy3(value, c):
    properties.set_algorithm(4, c)


def run_game():
    show_path = properties.get_pathing()
    player_alg = properties.get_player_algo(1)
    en1_alg = properties.get_player_algo(2)
    en2_alg = properties.get_player_algo(3)
    en3_alg = properties.get_player_algo(4)
    game.game_init(show_path, player_alg, en1_alg, en2_alg, en3_alg, TILE_SIZE)


def main_background():
    global surface
    surface.fill(COLOR_BACKGROUND)


def menu_loop():
    pygame.init()

    pygame.display.set_caption('Bomberman')
    clock = pygame.time.Clock()

    menu_theme = pygame_menu.themes.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=int(TILE_SIZE*0.8),
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.7),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR
    )

    play_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * 0.7),
        width=int(WINDOW_SIZE[0] * 0.7),
        onclose=pygame_menu.events.NONE,
        title='Play menu'
    )

    play_options = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * 0.7),
        width=int(WINDOW_SIZE[0] * 0.7),
        title='Options'
    )
    play_options.add.selector("Character 1", [("Player", Algorithm.PLAYER), ("DFS", Algorithm.DFS),
                                              ("DIJKSTRA", Algorithm.DIJKSTRA), ("None", Algorithm.NONE)], onchange=change_player)
    play_options.add.selector("Character 2", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("None", Algorithm.NONE)], onchange=change_enemy1)
    play_options.add.selector("Character 3", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("None", Algorithm.NONE)], onchange=change_enemy2,  default=1)
    play_options.add.selector("Character 4", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("None", Algorithm.NONE)], onchange=change_enemy3)
    play_options.add.selector("Show path", [("Yes", True), ("No", False)], onchange=change_path)

    play_options.add.button('Back', pygame_menu.events.BACK)
    play_menu.add.button('Start',
                         run_game)

    play_menu.add.button('Options', play_options)
    play_menu.add.button('Return  to  main  menu', pygame_menu.events.BACK)

    about_menu_theme = pygame_menu.themes.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=TILE_SIZE,
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.4),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR
    )

    about_menu = pygame_menu.Menu(
        theme=about_menu_theme,
        height=int(WINDOW_SIZE[1] * 0.7),
        width=int(WINDOW_SIZE[0] * 0.7),
        onclose=pygame_menu.events.NONE,
        title='About'
    )
    about_menu.add.label("Player_controls: ")
    about_menu.add.label("Movement:_Arrows")
    about_menu.add.label("Plant bomb:_Space")
    about_menu.add.label("Author:_Michal_Sliwa")
    about_menu.add.label("Sprite: ")

    about_menu.add.label("https://opengameart.org/content")
    about_menu.add.label("/bomb-party-the-complete-set")

    main_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * 0.6),
        width=int(WINDOW_SIZE[0] * 0.6),
        onclose=pygame_menu.events.NONE,
        title='Main menu'
    )

    main_menu.add.button('Play', play_menu)
    main_menu.add.button('About', about_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    while True:

        clock.tick(FPS)

        main_background()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        main_menu.mainloop(surface, main_background, disable_loop=False, fps_limit=0)
        main_menu.update(events)
        main_menu.draw(surface)

        pygame.display.update()


menu_loop()
