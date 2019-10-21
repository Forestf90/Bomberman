import unittest
import game


class MyTestCase(unittest.TestCase):
    def test_map_generation_corners(self):
        game.generate_map()
        self.assertEqual(0, game.grid[1][1])
        self.assertEqual(0, game.grid[1][2])
        self.assertEqual(0, game.grid[2][1])

        l = len(game.grid)

        self.assertEqual(0, game.grid[l - 2][1])
        self.assertEqual(0, game.grid[l - 2][2])
        self.assertEqual(0, game.grid[l - 3][1])

        self.assertEqual(0, game.grid[1][l - 2])
        self.assertEqual(0, game.grid[1][l - 3])
        self.assertEqual(0, game.grid[2][l - 2])

        self.assertEqual(0, game.grid[l - 2][l - 2])
        self.assertEqual(0, game.grid[l - 2][l - 3])
        self.assertEqual(0, game.grid[l - 3][l - 2])


if __name__ == '__main__':
    unittest.main()

