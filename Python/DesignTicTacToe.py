class DesignTicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.horiz = [0]*n
        self.vert = [0]*n
        self.diag1 = 0
        self.diag2 = 0

    # O(1) to check which player win
    # O(n) as space complexity
    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        move = 1
        if player == 2:
            move = -1

        self.horiz[row] += move
        self.vert[col] += move

        if row == col:
            self.diag1 += move
        if row+col == (n-1):
            self.diag2 += move

        if abs(self.horiz[row]) == n or abs(self.vert[col]) == n or abs(self.diag1) == n or abs(self.diag2) == n:
            return player
        return 0
