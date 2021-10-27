import collections
from typing import List


class Maze:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = collections.deque([start])
        rows = len(maze)
        cols = len(maze[0])

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while queue:
            i, j = queue.popleft()
            maze[i][j] = 2

            if i == destination[0] and j == destination[1]:
                return True

            for x, y in dirs:
                row = i + x
                col = j + y

                while 0 <= row < rows and 0 <= col < cols and maze[row][col] != 1:
                    row += x
                    col += y

                # back up one step, cuz it's at wall right now
                row -= x
                col -= y

                if maze[row][col] == 0:
                    queue.append((row, col))

        return False
