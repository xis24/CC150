import random
from typing import List


class MyRand:
    def __init__(self, row, col, bombs):
        self.end = row * col - 1
        self.data = [i for i in range(row * col)]

    def getRandom(self):
        index = random.randint(0, self.end)
        ans = self.data[index]
        self.data[index] = -1
        self.data[index], self.data[self.end] = self.data[self.end], self.data[index]
        self.end -= 1
        return ans


class MineSweeper:

    def generateBoard(self, rows, cols, bombs):
        if not rows or not cols:
            return []
        if bombs < 0 and bombs >= rows * cols:
            return []

        board = [[0] * cols for _ in range(rows)]
        bombPos = []

        myRand = MyRand(rows, cols, bombs)
        while len(bombPos) < bombs:
            bombPos.append(myRand.getRandom())

        for k in bombPos:
            board[k // rows][k % cols] = 1
        return board

    # leetcode 529
    def updateBoard(self, board, click) -> List[List[str]]:
        if not board:
            return []

        x, y = click
        # if it's mine
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        self.dfs(x, y, board)
        return board

    def dfs(self, x, y, board):
        # not empty cell
        if board[x][y] != 'E':
            return
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]
        rows = len(board)
        cols = len(board[0])
        mineCount = 0
        for d in directions:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'M':
                mineCount += 1

        if mineCount == 0:
            board[x][y] = 'B'
        else:
            board[x][y] = mineCount
            return

        for d in directions:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < rows and 0 <= ny < cols:
                self.dfs(nx, ny, board)


if __name__ == '__main__':
    obj = MineSweeper()
    board = obj.generateBoard(4, 4, 10)
    for i in board:
        print(i)
