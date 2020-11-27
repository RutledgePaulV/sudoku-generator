class Solver:

    # constructor for a solver, keeps a local copy of provided board
    def __init__(self, board):
        self.board = board.copy()
        self.vacants = self.board.get_unused_cells()

    # checks to make sure each compartment contains
    def is_valid(self):
        valid = set(range(1, 10))
        for i, box in self.board.boxes.items():
            if not valid == set([x.value for x in box]):
                return False
        for i, row in self.board.rows.items():
            if not valid == set([x.value for x in row]):
                return False
        for i, col in self.board.columns.items():
            if not valid == set([x.value for x in col]):
                return False
        return True

    # solves a puzzle by moving forward and backwards through puzzle
    # and testing values
    def solve(self):
        index = 0
        while -1 < index < len(self.vacants):
            current = self.vacants[index]
            flag = False
            my_range = range(current.value + 1, 10)
            for x in my_range:
                if x in self.board.get_possibles(current):
                    current.value = x
                    flag = True
                    break
            if not flag:
                current.value = 0
                index -= 1
            else:
                index += 1
        if len(self.vacants) == 0:
            return False
        else:
            return index == len(self.vacants)
