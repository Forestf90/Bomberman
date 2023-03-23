import unittest

import game
from bomb import Bomb
from enemy import Enemy
from player import Player
from enums.algorithm import Algorithm


class MyTestCase(unittest.TestCase):

    def setUp(self):
        game.enemy_list.append(Enemy(11, 11, Algorithm.DFS))
        game.player = Player()

    def test_plant(self):
        bomb = game.player.plant_bomb(game.GRID_BASE)

        self.assertEqual(1, bomb.pos_x)
        self.assertEqual(1, bomb.pos_y)
        self.assertEqual(3, bomb.range)

    def test_get_range(self):

        bomb = game.player.plant_bomb(game.GRID_BASE)

        self.assertEqual(5, len(bomb.sectors))
        self.assertEqual(True, [1, 1] in bomb.sectors)
        self.assertEqual(True, [1, 2] in bomb.sectors)
        self.assertEqual(True, [2, 1] in bomb.sectors)
        self.assertEqual(True, [1, 3] in bomb.sectors)
        self.assertEqual(True, [3, 1] in bomb.sectors)

        self.assertEqual(False, [1, 0] in bomb.sectors)
        self.assertEqual(False, [0, 1] in bomb.sectors)

    def test_bomb_explode(self):
        temp_bomb = Bomb(3, 11, 11, game.GRID_BASE, game.enemy_list[0])
        game.bombs.append(temp_bomb)

        game.update_bombs(game.GRID_BASE, 2980)

        self.assertEqual(1, len(game.bombs))
        self.assertEqual(20, temp_bomb.time)

        game.update_bombs(game.GRID_BASE, 50)

        self.assertEqual(0, len(game.bombs))
        self.assertEqual(1, len(game.explosions))


if __name__ == '__main__':
    unittest.main()
