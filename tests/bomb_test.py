import unittest
import game
from bomb import Bomb
from enemy import Enemy
from player import Player


class MyTestCase(unittest.TestCase):

    def test_bomb_explode(self):

        en = Enemy(11, 11)
        game.player = Player()
        temp_bomb = Bomb(3, 1, 1, game.grid, en)
        game.bombs.append(temp_bomb)

        game.update_bombs(2980)

        self.assertEqual(1, len(game.bombs))
        self.assertEqual(20, temp_bomb.time)

        game.update_bombs(50)

        self.assertEqual(0, len(game.bombs))
        self.assertEqual(1, len(game.explosions))


if __name__ == '__main__':
    unittest.main()
