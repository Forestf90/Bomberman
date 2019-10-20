import pygame, pygameMenu
import game

COLOR_BACKGROUND = (153, 153, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (102, 102, 153)
MENU_TITLE_COLOR = (51, 51, 255)
WINDOW_SIZE = (13*40, 13*40)

clock = None
main_menu = None
algo = ["DFS", "BFS"]
en1_alg = 0
surface = pygame.display.set_mode(WINDOW_SIZE)


def main_background():
    global surface
    surface.fill(COLOR_BACKGROUND)

def menu_loop():

    pygame.init()

    pygame.display.set_caption('Bomberman')
    clock = pygame.time.Clock()

    # Play menu
    play_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOR_BLACK,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_color_title=MENU_TITLE_COLOR,
                                menu_height=int(WINDOW_SIZE[1] * 0.7),
                                menu_width=int(WINDOW_SIZE[0] * 0.7),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='Play menu',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )

    play_options = pygameMenu.Menu(surface,
                                   bgfun=main_background,
                                   color_selected=COLOR_WHITE,
                                   font=pygameMenu.font.FONT_BEBAS,
                                   font_color=COLOR_BLACK,
                                   font_size=30,
                                   menu_alpha=100,
                                   menu_color=MENU_BACKGROUND_COLOR,
                                   menu_color_title=MENU_TITLE_COLOR,
                                   menu_height=int(WINDOW_SIZE[1] * 0.7),
                                   menu_width=int(WINDOW_SIZE[0] * 0.7),
                                   option_shadow=False,
                                   title='Options',
                                   window_height=WINDOW_SIZE[1],
                                   window_width=WINDOW_SIZE[0]
                                   )
    play_options.add_selector("Character 1", [("Player", 2), ("DFS", 0), ("BFS", 1)])
    play_options.add_selector("Character 2", [("DFS", 0), ("BFS", 1)])
    play_options.add_selector("Character 3", [("DFS", 0), ("BFS", 1)])
    play_options.add_selector("Character 4", [("DFS", 0), ("BFS", 1)])
    play_options.add_selector("Show path", [("Yes", True), ("No", False)])
    play_options.add_option('Back', pygameMenu.events.BACK)
    play_menu.add_option('Start',  # When pressing return -> play(DIFFICULTY[0], font)
                         game.game_init,
                         # DIFFICULTY,
                         # pygame.font.Font(pygameMenu.font.FONT_FRANCHISE, 30)
                         )

    play_menu.add_option('Options', play_options)
    play_menu.add_option('Return to main menu', pygameMenu.events.BACK)
    # About menu
    about_menu = pygameMenu.TextMenu(surface,
                                     bgfun=main_background,
                                     color_selected=COLOR_WHITE,
                                     font=pygameMenu.font.FONT_BEBAS,
                                     font_color=COLOR_BLACK,
                                     font_size_title=30,
                                     font_title=pygameMenu.font.FONT_BEBAS,
                                     menu_color=MENU_BACKGROUND_COLOR,
                                     menu_color_title=MENU_TITLE_COLOR,
                                     menu_height=int(WINDOW_SIZE[1] * 0.7),
                                     menu_width=int(WINDOW_SIZE[0] * 0.7),
                                     onclose=pygameMenu.events.DISABLE_CLOSE,
                                     option_shadow=False,
                                     text_color=COLOR_BLACK,
                                     text_fontsize=17,
                                     title='About',
                                     window_height=WINDOW_SIZE[1],
                                     window_width=WINDOW_SIZE[0]
                                     )
    about_menu.add_line("Author:  Michal Sliwa")
    about_menu.add_line("Sprite : ")
    about_menu.add_line("Original Bomb Party sprite sheet by")
    about_menu.add_line("Matt Hackett of Lost Decade Games,")
    about_menu.add_line("expanded by Cem Kalyoncu and /usr/share.")
    about_menu.add_line("Link :")
    about_menu.add_line("https://opengameart.org/content")
    about_menu.add_line("/bomb-party-the-complete-set")
    # Main menu
    main_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOR_BLACK,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_color_title=MENU_TITLE_COLOR,
                                menu_height=int(WINDOW_SIZE[1] * 0.6),
                                menu_width=int(WINDOW_SIZE[0] * 0.6),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='Main menu',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )

    main_menu.add_option('Play', play_menu)
    main_menu.add_option('About', about_menu)
    main_menu.add_option('Quit', pygameMenu.events.EXIT)
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Main menu
        main_menu.mainloop(events)

        # Flip surface
        pygame.display.flip()




menu_loop()