import collections
from typing import List
import heapq


class Maze:

    # BFS
    # Time Complexity O(mn)
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

    # dijkstra algo to find the shorted path
    # heap to choose the shorted distance, and stopped to acted as visited
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        queue = [(0, start[0], start[1])]
        stopped = {(start[0], start[1]): 0}

        while queue:
            dist, x, y = heapq.heappop(queue)
            if [x, y] == destination:
                return dist

            for i, j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                newX, newY, d = x, y, 0
                while 0 <= newX + i < rows and 0 <= newY + j < cols and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                if (newX, newY) not in stopped or dist + d < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = dist + d
                    heapq.heappush(queue, (dist + d, newX, newY))

        return -1
