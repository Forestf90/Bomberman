import unittest

import game
from bomb import Bomb
from enemy import Enemy
from player import Player


class MyTestCase(unittest.TestCase):

    def setUp(self):
        game.enemy_list.append(Enemy(11, 11))
        game.player = Player()

    def test_plant(self):
        bomb = game.player.plant_bomb(game.grid)

        self.assertEqual(1, bomb.posX)
        self.assertEqual(1, bomb.posY)
        self.assertEqual(3, bomb.range)

    def test_bomb_explode(self):
        # en = Enemy(11, 11)
        # game.player = Player()
        temp_bomb = Bomb(3, 11, 11, game.grid, game.enemy_list[0])
        game.bombs.append(temp_bomb)

        game.update_bombs(2980)

        self.assertEqual(1, len(game.bombs))
        self.assertEqual(20, temp_bomb.time)

        game.update_bombs(50)

        self.assertEqual(0, len(game.bombs))
        self.assertEqual(1, len(game.explosions))

    def test_death(self):
        bomb = Bomb(3, 1, 2, game.grid, game.player)
        game.bombs.append(bomb)
        game.update_bombs(1500)
        self.assertEqual(True, game.player.life)
        self.assertEqual(0, len(game.explosions))

        game.update_bombs(1501)
        self.assertEqual(False, game.player.life)
        self.assertEqual(0, len(game.explosions))


if __name__ == '__main__':
    unittest.main()
