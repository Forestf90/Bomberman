class Node:

    parent = None

    def __init__(self, px, py, reach, weight, value):
        self.x = px
        self.y = py
        self.reach = reach
        self.weight = weight
        self.value = value

