import pygame
import pygame_menu

import game
from algorithm import Algorithm

COLOR_BACKGROUND = (153, 153, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (102, 102, 153)
MENU_TITLE_COLOR = (51, 51, 255)

pygame.display.init()
INFO = pygame.display.Info()
TILE_SIZE = int(INFO.current_h * 0.035)
WINDOW_SIZE = (13 * TILE_SIZE, 13 * TILE_SIZE)

clock = None
player_alg = Algorithm.PLAYER
en1_alg = Algorithm.DIJKSTRA
en2_alg = Algorithm.DFS
en3_alg = Algorithm.DIJKSTRA
show_path = True
surface = pygame.display.set_mode(WINDOW_SIZE)


def change_path(value, c):
    global show_path
    show_path = c


def change_player(value, c):
    global player_alg
    player_alg = c


def change_enemy1(value, c):
    global en1_alg
    en1_alg = c


def change_enemy2(value, c):
    global en2_alg
    en2_alg = c


def change_enemy3(value, c):
    global en3_alg
    en3_alg = c


def run_game():
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
        title_background_color=MENU_TITLE_COLOR,
        widget_shadow=False
    )

    play_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * 0.7),
        width=int(WINDOW_SIZE[0] * 0.7),
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Play menu'
    )

    play_options = pygame_menu.Menu(theme=menu_theme,
        height=int(WINDOW_SIZE[1] * 0.7),
        width=int(WINDOW_SIZE[0] * 0.7),
        title='Options'
    )
    play_options.add_selector("Character 1", [("Player", Algorithm.PLAYER), ("DFS", Algorithm.DFS),
                                              ("DIJKSTRA", Algorithm.DIJKSTRA), ("None", Algorithm.NONE)], onchange=change_player)
    play_options.add_selector("Character 2", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("None", Algorithm.NONE)], onchange=change_enemy1)
    play_options.add_selector("Character 3", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("None", Algorithm.NONE)], onchange=change_enemy2,  default=1)
    play_options.add_selector("Character 4", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("None", Algorithm.NONE)], onchange=change_enemy3)
    play_options.add_selector("Show path", [("Yes", True), ("No", False)], onchange=change_path)

    play_options.add_button('Back', pygame_menu.events.BACK)
    play_menu.add_button('Start',
                         run_game)

    play_menu.add_button('Options', play_options)
    play_menu.add_button('Return  to  main  menu', pygame_menu.events.BACK)

    about_menu_theme = pygame_menu.themes.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=TILE_SIZE,
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.4),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR,
        widget_shadow=False
    )

    about_menu = pygame_menu.Menu(theme=about_menu_theme,
        height=int(WINDOW_SIZE[1] * 0.7),
        width=int(WINDOW_SIZE[0] * 0.7),
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='About'
    )
    about_menu.add_label("Player_controls: ")
    about_menu.add_label("Movement:_Arrows")
    about_menu.add_label("Plant bomb:_Space")
    about_menu.add_label("Author:_Michal_Sliwa")
    about_menu.add_label("Sprite: ")

    about_menu.add_label("https://opengameart.org/content")
    about_menu.add_label("/bomb-party-the-complete-set")

    main_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * 0.6),
        width=int(WINDOW_SIZE[0] * 0.6),
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Main menu'
    )

    main_menu.add_button('Play', play_menu)
    main_menu.add_button('About', about_menu)
    main_menu.add_button('Quit', pygame_menu.events.EXIT)
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

        pygame.display.flip()


menu_loop()
