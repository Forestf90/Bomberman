import pygame
from Players.AI.algorithm import Algorithm

player_alg = Algorithm.PLAYER
en1_alg = Algorithm.DIJKSTRA
en2_alg = Algorithm.DFS
en3_alg = Algorithm.DIJKSTRA
show_path = True


def singleton(cls):
    instances = dict()

    def wrapper():
        if cls not in instances:
            instances[cls] = cls()
        return instances.get(cls)

    return wrapper


@singleton
class Properties:
    def __init__(self, showpath: bool = show_path,
                 plr_1_alg: int = player_alg,
                 plr_2_alg: int = en1_alg,
                 plr_3_alg: int = en2_alg,
                 plr_4_alg: int = en3_alg):
        self.show_path = showpath
        self.players_algorithms = {1: plr_1_alg, 2: plr_2_alg, 3: plr_3_alg, 4: plr_4_alg}

    def set_algorithm(self, player: int, alg: bool):
        self.players_algorithms[player] = alg

    def set_pathing(self, pathing):
        self.show_path = pathing

    def get_pathing(self):
        return self.show_path

    def get_player_algo(self, player):
        return self.players_algorithms.get(player)
