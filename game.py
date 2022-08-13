import pygame
import pygame_menu
import sys
import random
import time
from copy import deepcopy
from Players.player import Player
from Bombs.explosion import Explosion
from Players.enemy import Enemy
from Players.AI.algorithm import Algorithm
from ingame_properties import Properties


properties = Properties()


TILE_WIDTH = 40
TILE_HEIGHT = 40

WINDOW_WIDTH = 13 * TILE_WIDTH
WINDOW_HEIGHT = 13 * TILE_HEIGHT
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
BACKGROUND = (107, 142, 35)
MENU_BACKGROUND_COLOR = (52, 78, 91)
MENU_TITLE_COLOR = (102, 102, 153)

pygame.display.init()
INFO = pygame.display.Info()
TILE_SIZE = int(INFO.current_h * 0.035)
MENU_TILE_SIZE = 40


surface = None
show_path = True

clock = None

player = None
enemy_list = []
ene_blocks = []
bombs = []
explosions = []

init_grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
grid = deepcopy(init_grid)

grass_img = None
block_img = None
box_img = None
bomb1_img = None
bomb2_img = None
bomb3_img = None
explosion1_img = None
explosion2_img = None
explosion3_img = None


terrain_images = []
bomb_images = []
explosion_images = []

pygame.font.init()
font = pygame.font.SysFont('Bebas', 30)
# TEXT_LOSE = font.render('GAME OVER', False, (0, 0, 0))
# TEXT_WIN = font.render('WIN', False, (0, 0, 0))

game_running = True


def set_game_state(state):
    global game_running
    game_running = state


def pause():
    paused = True

    def unpause():
        nonlocal paused
        paused = False

    def restart():
        unpause()
        game_over(restart=True)

    def main_menu():
        unpause()
        set_game_state(False)

    menu_theme = pygame_menu.themes.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=int(MENU_TILE_SIZE * 0.8),
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(MENU_TILE_SIZE * 0.7),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR
    )

    pause_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * 0.5),
        width=int(WINDOW_SIZE[0] * 0.5),
        onclose=pygame_menu.events.NONE,
        title='Paused'
    )

    pause_menu.add.button('Resume', unpause)
    pause_menu.add.button('Restart', restart)
    pause_menu.add.button('Return to main menu', main_menu)

    while paused:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    unpause()

        pause_menu.update(events)
        pause_menu.draw(surface)

        pygame.display.update()


def game_init(path, player_alg, en1_alg, en2_alg, en3_alg, scale):

    global TILE_WIDTH
    global TILE_HEIGHT
    TILE_WIDTH = scale
    TILE_HEIGHT = scale

    global font
    font = pygame.font.SysFont('Bebas', scale)

    global show_path
    show_path = path

    global surface
    surface = pygame.display.set_mode((13 * TILE_WIDTH, 13 * TILE_HEIGHT))
    pygame.display.set_caption('Bomberman')

    global clock
    clock = pygame.time.Clock()

    global enemy_list
    global ene_blocks
    global player

    enemy_list = []
    ene_blocks = []
    global explosions
    global bombs
    bombs.clear()
    explosions.clear()

    player = Player()

    if en1_alg is not Algorithm.NONE:
        en1 = Enemy(11, 11, en1_alg)
        en1.load_animations('1', scale)
        enemy_list.append(en1)
        ene_blocks.append(en1)

    if en2_alg is not Algorithm.NONE:
        en2 = Enemy(1, 11, en2_alg)
        en2.load_animations('2', scale)
        enemy_list.append(en2)
        ene_blocks.append(en2)

    if en3_alg is not Algorithm.NONE:
        en3 = Enemy(11, 1, en3_alg)
        en3.load_animations('3', scale)
        enemy_list.append(en3)
        ene_blocks.append(en3)

    if player_alg is Algorithm.PLAYER:
        player.load_animations(scale)
        ene_blocks.append(player)
    elif player_alg is not Algorithm.NONE:
        en0 = Enemy(1, 1, player_alg)
        en0.load_animations('', scale)
        enemy_list.append(en0)
        ene_blocks.append(en0)
        player.life = False
    else:
        player.life = False

    global grass_img
    grass_img = pygame.image.load('images/terrain/grass.png')
    grass_img = pygame.transform.scale(grass_img, (TILE_WIDTH, TILE_HEIGHT))
    global block_img
    block_img = pygame.image.load('images/terrain/block.png')
    block_img = pygame.transform.scale(block_img, (TILE_WIDTH, TILE_HEIGHT))
    global box_img
    box_img = pygame.image.load('images/terrain/box.png')
    box_img = pygame.transform.scale(box_img, (TILE_WIDTH, TILE_HEIGHT))
    global bomb1_img
    bomb1_img = pygame.image.load('images/bomb/1.png')
    bomb1_img = pygame.transform.scale(bomb1_img, (TILE_WIDTH, TILE_HEIGHT))
    global bomb2_img
    bomb2_img = pygame.image.load('images/bomb/2.png')
    bomb2_img = pygame.transform.scale(bomb2_img, (TILE_WIDTH, TILE_HEIGHT))
    global bomb3_img
    bomb3_img = pygame.image.load('images/bomb/3.png')
    bomb3_img = pygame.transform.scale(bomb3_img, (TILE_WIDTH, TILE_HEIGHT))
    global explosion1_img
    explosion1_img = pygame.image.load('images/explosion/1.png')
    explosion1_img = pygame.transform.scale(explosion1_img, (TILE_WIDTH, TILE_HEIGHT))
    global explosion2_img
    explosion2_img = pygame.image.load('images/explosion/2.png')
    explosion2_img = pygame.transform.scale(explosion2_img, (TILE_WIDTH, TILE_HEIGHT))
    global explosion3_img
    explosion3_img = pygame.image.load('images/explosion/3.png')
    explosion3_img = pygame.transform.scale(explosion3_img, (TILE_WIDTH, TILE_HEIGHT))
    global terrain_images
    terrain_images = [grass_img, block_img, box_img, grass_img]
    global bomb_images
    bomb_images = [bomb1_img, bomb2_img, bomb3_img]
    global explosion_images
    explosion_images = [explosion1_img, explosion2_img, explosion3_img]

    main()


def draw():
    surface.fill(BACKGROUND)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            surface.blit(terrain_images[grid[i][j]], (i * TILE_WIDTH, j * TILE_HEIGHT, TILE_HEIGHT, TILE_WIDTH))

    for x in bombs:
        surface.blit(bomb_images[x.frame], (x.posX * TILE_WIDTH, x.posY * TILE_HEIGHT, TILE_HEIGHT, TILE_WIDTH))

    for y in explosions:
        for x in y.sectors:
            surface.blit(explosion_images[y.frame], (x[0] * TILE_WIDTH, x[1] * TILE_HEIGHT, TILE_HEIGHT, TILE_WIDTH))
    if player.life:
        surface.blit(player.animation[player.direction][player.frame],
                     (player.posX * (TILE_WIDTH / 4), player.posY * (TILE_HEIGHT / 4), TILE_WIDTH, TILE_HEIGHT))
    for en in enemy_list:
        if en.life:
            surface.blit(en.animation[en.direction][en.frame],
                         (en.posX * (TILE_WIDTH / 4), en.posY * (TILE_HEIGHT / 4), TILE_WIDTH, TILE_HEIGHT))
            if show_path:
                if en.algorithm == Algorithm.DFS:
                    for sek in en.path:
                        pygame.draw.rect(surface, (255, 0, 0, 240), [sek[0] * TILE_WIDTH, sek[1] * TILE_HEIGHT, TILE_WIDTH, TILE_WIDTH], 1)
                else:
                    for sek in en.path:
                        pygame.draw.rect(surface, (255, 0, 255, 240), [sek[0] * TILE_WIDTH, sek[1] * TILE_HEIGHT, TILE_WIDTH, TILE_WIDTH], 1)

    pygame.display.update()


def generate_map():
    global grid
    grid = deepcopy(init_grid)

    for i in range(1, len(init_grid) - 1):
        for j in range(1, len(init_grid[i]) - 1):
            if init_grid[i][j] != 0:
                continue
            elif (i < 3 or i > len(init_grid) - 4) and (j < 3 or j > len(init_grid[i]) - 4):
                continue
            if random.randint(0, 90) < 72:
                grid[i][j] = 2

    return


def main():
    set_game_state(True)

    generate_map()
    # while player.life:
    while game_running:
        dt = clock.tick(20)  # will play with it a little
        update_bombs(dt)
        count = 0
        winner = ""
        for en in ene_blocks:
            if isinstance(en, Enemy):
                en.make_move(grid, bombs, explosions, ene_blocks)
            if en.life:
                count += 1
                winner = en.get_name()

        if check_winner(count, winner):
            break

        keys = pygame.key.get_pressed()
        temp = player.direction
        movement = False
        if keys[pygame.K_DOWN]:
            temp = 0
            player.move(0, 1, grid, ene_blocks)
            movement = True
        elif keys[pygame.K_RIGHT]:
            temp = 1
            player.move(1, 0, grid, ene_blocks)
            movement = True
        elif keys[pygame.K_UP]:
            temp = 2
            player.move(0, -1, grid, ene_blocks)
            movement = True
        elif keys[pygame.K_LEFT]:
            temp = 3
            player.move(-1, 0, grid, ene_blocks)
            movement = True
        if temp != player.direction:
            player.frame = 0
            player.direction = temp
        if movement:
            if player.frame == 2:
                player.frame = 0
            else:
                player.frame += 1

        draw()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    if player.bomb_limit == 0:
                        continue
                    temp_bomb = player.plant_bomb(grid)
                    bombs.append(temp_bomb)
                    grid[temp_bomb.posX][temp_bomb.posY] = 3
                    player.bomb_limit -= 1

                elif e.key == pygame.K_ESCAPE:
                    pause()

    game_over()


def check_winner(count, winner):
    if count < 2:
        draw()
        if count == 1:
            textsurface = font.render(winner + " wins", False, (0, 0, 0), (255, 255, 255))
        if count == 0:
            textsurface = font.render("Draw", False, (0, 0, 0), (255, 255, 255))

        font_w = textsurface.get_width()
        font_h = textsurface.get_height()
        surface.blit(textsurface, (surface.get_width() // 2 - font_w // 2, surface.get_height() // 2 - font_h // 2))
        pygame.display.update()
        time.sleep(2)

        set_game_state(False)

        return True
    else:
        return False


def update_bombs(dt):
    for b in bombs:
        b.update(dt)
        if b.time < 1:
            b.bomber.bomb_limit += 1
            grid[b.posX][b.posY] = 0
            exp_temp = Explosion(b.posX, b.posY, b.range)
            exp_temp.explode(grid, bombs, b)
            exp_temp.clear_sectors(grid)
            explosions.append(exp_temp)
    if player not in enemy_list:
        player.check_death(explosions)
    for en in enemy_list:
        en.check_death(explosions)
    for e in explosions:
        e.update(dt)
        if e.time < 1:
            explosions.remove(e)


def game_over(restart=False):
    draw()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
    explosions.clear()
    enemy_list.clear()
    ene_blocks.clear()

    if restart:
        show_path = properties.get_pathing()
        player_alg = properties.get_player_algo(1)
        en1_alg = properties.get_player_algo(2)
        en2_alg = properties.get_player_algo(3)
        en3_alg = properties.get_player_algo(4)
        game_init(show_path, player_alg, en1_alg, en2_alg, en3_alg, TILE_SIZE)
