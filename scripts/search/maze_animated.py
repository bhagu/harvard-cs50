import time
import os

class Maze:
    def __init__(self):
        self.height = 5
        self.width = 5
        self.walls = [
            [True,  True,  True,  True,  True ],
            [True,  False, False, False, True ],
            [True,  False, True,  False, True ],
            [True,  False, True,  False, False],
            [True,  True,  True,  True,  True ]
        ]
        self.start = (3, 1)
        self.goal = (3, 4)
        self.solution = [(1, 2), (1, 3), (2, 3)]  # Sample path

    def print_animated(self):
        for step in range(len(self.solution) + 1):
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(self.height):
                for j in range(self.width):
                    if self.walls[i][j]:
                        print("█", end="")
                    elif (i, j) == self.start:
                        print("A", end="")
                    elif (i, j) == self.goal:
                        print("B", end="")
                    elif (i, j) in self.solution[:step]:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print()
            time.sleep(2)

# Run animation
maze = Maze()
maze.print_animated()