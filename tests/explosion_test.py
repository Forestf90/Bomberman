import unittest
import game

from bomb import Bomb
from enemy import Enemy
from player import Player


class MyTestCase(unittest.TestCase):

    def setUp(self):
        game.enemy_list.append(Enemy(11, 11))
        game.enemy_list.append(Enemy(1, 2))
        game.player = Player()

    def test_explosion_sectors(self):

        enemy = game.enemy_list[0]
        game.bombs.append(enemy.plant_bomb(game.grid))
        game.update_bombs(2980)
        game.update_bombs(50)

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


if __name__ == '__main__':
    unittest.main()
