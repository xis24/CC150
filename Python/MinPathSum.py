from typing import List


class MinPathSum:

    # Time: O(m * n)
    # Space: O(m * n)
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[grid[0][0] for _ in range(cols)] for _ in range(rows)]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, cols):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][cols - 1]

    # Time: O(m*n)
    # Space: O(n)
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [0] * cols
        dp[0] = grid[0][0]

        for j in range(1, cols):
            dp[j] = dp[j - 1] + grid[0][j]

        for i in range(1, rows):
            dp[0] = grid[i][0]
            for j in range(1, cols):
                # either the current one or left one column
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[cols - 1]

    # Time: O(m * n)
    # Space: O(1)
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]

        for j in range(1, cols):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[rows - 1][cols - 1]
