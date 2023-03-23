import unittest
import game

from enemy import Enemy
from player import Player
from enums.algorithm import Algorithm


class MyTestCase(unittest.TestCase):

    def setUp(self):
        game.enemy_list.append(Enemy(11, 11, Algorithm.DFS))
        game.enemy_list.append(Enemy(1, 11, Algorithm.DIJKSTRA))
        game.player = Player()

    def test_explosion_sectors(self):

        enemy = game.enemy_list[0]
        game.bombs.append(enemy.plant_bomb(game.GRID_BASE))
        game.update_bombs(game.GRID_BASE, 2980)
        game.update_bombs(game.GRID_BASE, 50)

        self.assertEqual(1, len(game.explosions))
        exp = game.explosions[0]

        self.assertEqual(5, len(exp.sectors))
        self.assertEqual(True, [11, 11] in exp.sectors)
        self.assertEqual(True, [11, 10] in exp.sectors)
        self.assertEqual(True, [10, 11] in exp.sectors)
        self.assertEqual(True, [11, 9] in exp.sectors)
        self.assertEqual(True, [9, 11] in exp.sectors)

        self.assertEqual(False, [11, 12] in exp.sectors)
        self.assertEqual(False, [12, 11] in exp.sectors)

    def test_box_destroy(self):

        game.GRID_BASE[2][1] = 2
        self.assertEqual(2, game.GRID_BASE[2][1])
        game.bombs.append(game.player.plant_bomb(game.GRID_BASE))
        game.update_bombs(game.GRID_BASE, 2980)
        game.update_bombs(game.GRID_BASE, 50)

        self.assertEqual(0, game.GRID_BASE[2][1])
        self.assertEqual(True, [2, 1] in game.explosions[0].sectors)

    def test_death(self):
        en = game.enemy_list[1]
        game.bombs.append(en.plant_bomb(game.GRID_BASE))
        game.update_bombs(game.GRID_BASE, 1500)
        self.assertEqual(True, en.life)
        self.assertEqual(0, len(game.explosions))

        game.update_bombs(game.GRID_BASE, 1501)
        self.assertEqual(False, en.life)
        self.assertEqual(0, len(game.explosions))


if __name__ == '__main__':
    unittest.main()
