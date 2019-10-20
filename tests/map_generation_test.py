import unittest
import game


class MyTestCase(unittest.TestCase):
    def map_generation_corners(self):
        game.generate_map()
        self.assertEqual(game.map[1][1], 1)
        self.assertEqual(game.map[1][2], 1)
        self.assertEqual(game.map[2][1], 1)

        l = len(map)

        self.assertEqual(game.map[l-1][1], 1)
        self.assertEqual(game.map[l-1][2], 1)
        self.assertEqual(game.map[l-2][1], 1)

        self.assertEqual(game.map[1][l-1], 1)
        self.assertEqual(game.map[1][l-2], 1)
        self.assertEqual(game.map[2][l-1], 1)

        self.assertEqual(game.map[l - 1][l-1], 1)
        self.assertEqual(game.map[l - 1][l-2], 1)
        self.assertEqual(game.map[l - 2][l-1], 1)


if __name__ == '__main__':
    unittest.main()
