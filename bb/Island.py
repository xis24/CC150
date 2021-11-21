from typing import List
from collections import deque


class IslandPerimeters:

    # For each of island (grid[i][j] == 1), we check four direction: if any of cell is also a island, we just denote as 1.
    # we calculate the sum of up, down, left, right. For each island, 4 - sum(up, down, left, right) will be the perimeter
    # then we sum up all the island
    # Time O(m * n)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    up = 0 if r == 0 else grid[r - 1][0]
                    down = 0 if r == rows - 1 else grid[r + 1][0]
                    left = 0 if c == 0 else grid[r][c - 1]
                    right = 0 if c == cols - 1 else grid[r][c + 1]
                    result += 4 - sum(up, down, left, right)
        return result

    # slightly better approach:
    # Since we are scanning from up to down, from left and right, we only need do two comparision: check if up and left cell is an island,
    # if yes, we need to substract 2 (cuz each cell will decrease edge by 1)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    if r > 0 and grid[r - 1][c] == 1:
                        result -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        result -= 2
        return result

    # We can actually calculate the how many the boudary cell we have.
    # for each cell, we check four directions to see if any direction is a boundary
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        DIR = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for offsetX, offsetY in DIR:
                        nr = r + offsetX
                        nc = c + offsetY
                        if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] == 0:
                            res += 1
        return res


class NumberOfIsland:

    # Time O(nm)
    # Space O(nm)
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * cols for _ in range(rows)]
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    count += 1
                    self.dfs(r, c, grid, visited)
        return count

    def dfs(self, row, col, grid, visited):
        visited[row][col] = True
        for offsetX, offsetY in self.DIR:
            newRow = row + offsetX
            newCol = col + offsetY
            if self.isValid(newRow, newCol, grid, visited):
                self.dfs(newRow, newCol, grid, visited)

    def isValid(self, row, col, grid, visisted):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and not visisted[row][col] and grid[row][col] == '1'

    # BFS with modified input
    def bfs(self, row, col, grid):
        queue = deque([(row, col)])
        grid[row][col] = '-1'
        while queue:
            x, y = queue.popleft()
            for offsetX, offsetY in self.DIR:
                newRow = x + offsetX
                newCol = y + offsetY
                if self.isValid(newRow, newCol, grid):
                    grid[newRow][newCol] = '-1'
                    queue.append((newRow, newCol))


class UnionFind:
    def __init__(self, n):
        self.count = 0
        self.parent = {}
        self.rank = [0] * n  # union by rank

    def __len__(self):
        return self.count

    def find(self, p):
        while p != self.parent[p]:
            # path compression
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i != j:
            if self.rank[i] < self.rank[j]:
                i, j = j, i
            self.parent[j] = i
            if self.rank[i] == self.rank[j]:
                self.rank[i] += 1
            self.count -= 1

    def setParent(self, x):
        if self.parent.get(x):
            return
        self.parent[x] = x
        self.count += 1


class NumberOfIslandTwo:
    # Assume all grid are water initially, given list of position of land,
    # You need to calculate the number of island after each insert of land. Return an array of result

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        disjoint_set = UnionFind(m * n)

        res = []
        for x, y in positions:
            idx = x * n + y
            disjoint_set.setParent(idx)
            for i, j in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and i * n + j in disjoint_set.parent:
                    disjoint_set.union(idx, i * n + j)

            res.append(len(disjoint_set))
        return res


class MaxAreaIsland:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curCount = self.bfs(grid, r, c)
                    count = max(curCount, count)
        return count

    def bfs(self, grid, r, c):
        count = 1
        grid[r][c] = 0
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(r, c)])

        while queue:
            row, col = queue.popleft()
            for offsetX, offsetY in DIR:
                newRow = row + offsetX
                newCol = col + offsetY

                if self.isValid(newRow, newCol, grid):
                    count += 1
                    grid[newRow][newCol] = 0
                    queue.append((newRow, newCol))

        return count

    def isValid(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1


class NumberOfDistinctIslands:
    '''
    Brute Force Solution:
    1. from left to right, top to bottom, get all islands
    2. compare each island with another to check if it's unique
    3. add to the result if it's unique
    Time: O(n^2 m^2) since we need to traverse the whole matrix, and for each island we need compare with others as well. worst case, each cell is an island. As a result O(mn) comparison
    Space: O(nm)
    '''

    # instead, we could save the LOCAL coordinates of each island, add this to a set
    # Time: O(mn)
    # Space: O(mn)
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        seen = set()  # visited set to avoid cycle
        unique_islands = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_island = set()
                row_origin = row
                col_origin = col
                self.dfs(row, col, row_origin, col_origin,
                         grid, seen, current_island)
                if current_island:
                    unique_islands.add(frozenset(current_island))
        return len(unique_islands)

    def dfs(self, row, col, row_origin, col_origin, grid, seen, current_island):
        if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
            return
        if (row, col) in seen or grid[row][col] == 0:
            return
        seen.add((row, col))
        current_island.add((row - row_origin, col - col_origin))
        self.dfs(row - 1, col, row_origin, col_origin,
                 grid, seen, current_island)
        self.dfs(row + 1, col, row_origin, col_origin,
                 grid, seen, current_island)
        self.dfs(row, col - 1, row_origin, col_origin,
                 grid, seen, current_island)
        self.dfs(row, col + 1, row_origin, col_origin,
                 grid, seen, current_island)

    # we could also save the path, like R, L, U, D
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        seen = set()
        unique_island = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                path = []
                self.dfs(row, col, grid, path, seen, "0")
                if path:
                    # have to use tuple instead of frozenset above, becausae there is dup direction, say RLUL
                    unique_island.add(tuple(path))
        return len(unique_island)

    def dfs(self, row, col, grid, path, seen, direction):
        if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
            return
        if (row, col) in seen or grid[row][col] == 0:
            return
        seen.add((row, col))
        path.append(direction)
        self.dfs(row + 1, col, grid, path, seen, "D")
        self.dfs(row - 1, col, grid, path, seen, "U")
        self.dfs(row, col + 1, grid, path, seen, "R")
        self.dfs(row, col - 1, grid, path, seen, "L")
        path.append("0")
