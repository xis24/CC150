from typing import List
import math
import collections


class ShortestDistanceFromAllBuilding:
    # approach one, from every empty land, do BFS to find all houses, get the min steps
    # NEED TO HAVE VISITED MATRIX
    # Time complexity O(n^2 * M^2)
    # Space O(n * m)

    # approach two, from every house, do BFS and mark matrix with (steps, number of house that can be reached)
    # In the end, traverse again the matrix and find the min value
    # with number of buildings
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        minDistance = math.inf
        totalhouse = 0

        # store (total_dist, house_count) for each cell
        distances = [[[0, 0] for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.bfs(grid, distances, i, j, totalhouse)
                    totalhouse += 1

        for i in range(rows):
            for j in range(cols):
                if distances[i][j][1] == totalhouse:
                    minDistance = min(minDistance, distances[i][j][0])

        return minDistance if minDistance != math.inf else -1

    def bfs(self, grid, distances, row, col, currentCount):
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = collections.deque([(row, col, 0)])
        while queue:
            x, y, step = queue.popleft()
            for offsetX, offsetY in dir:
                newX = x + offsetX
                newY = y + offsetY
                if self.isValid(newX, newY, grid, distances, currentCount):
                    distances[newX][newY][0] += step + 1
                    distances[newX][newY][1] = currentCount + 1
                    queue.append((newX, newY, step + 1))

    def isValid(self, x, y, grid, distance, count):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and distance[x][y][1] == count

    # approach three
    # 1. In stead of using visited matrix, we can decrement empty land (0) by 1.
    # 2. After each BFS, we decrement emptyLandValue (initially as 0) by 1. Then we will traverse all empty land cell with values equal
    # to emptyLandValue.
    # 3. After the last BFS, if min sitance is MAX, we return -1
    # 4. else we return min distance

    def shortestDistance(self, grid: List[List[int]]) -> int:
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        # total matrix to store total distance sum for each empty list
        total = [[0] * cols for _ in range(rows)]

        emptyLandValue = 0
        minDist = math.inf

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    minDist = math.inf
                    queue = collections.deque(([i, j]))
                    steps = 0

                    while queue:
                        steps += 1
                        level = len(queue)
                        for k in range(level):
                            x, y = queue.popleft()

                            for offsetX, offsetY in dir:
                                xx = offsetX + x
                                yy = offsetY + y

                                if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == emptyLandValue:
                                    grid[xx][yy] -= 1
                                    total[xx][yy] += steps
                                    queue.append((xx, yy))
                                    minDist = min(minDist, total[xx][yy])
                    emptyLandValue -= 1
        return minDist if minDist != math.inf else -1
