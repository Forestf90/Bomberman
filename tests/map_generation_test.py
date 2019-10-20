import unittest
import game


class MyTestCase(unittest.TestCase):
    def test_map_generation_corners(self):
        game.generate_map()
        self.assertEqual(0, game.map[1][1])
        self.assertEqual(0, game.map[1][2])
        self.assertEqual(0, game.map[2][1])

        l = len(game.map)

        self.assertEqual(0, game.map[l-2][1])
        self.assertEqual(0, game.map[l-2][2])
        self.assertEqual(0, game.map[l-3][1])

        self.assertEqual(0, game.map[1][l-2])
        self.assertEqual(0, game.map[1][l-3])
        self.assertEqual(0, game.map[2][l-2])

        self.assertEqual(0, game.map[l - 2][l-2])
        self.assertEqual(0, game.map[l - 2][l-3])
        self.assertEqual(0, game.map[l - 3][l-2])


if __name__ == '__main__':
    unittest.main()
    this.map_generation_corners_test()
