from typing import List


class FrogJump:

    # Brute force
    # Time: O(3 ^ n)
    # Space: O(n)
    def canCross(self, stones: List[int]) -> bool:
        return self.dfs(stones, 0, 0)

    # current pos, current jumpSize
    def dfs(self, stones, pos, jumpSize):
        if pos == len(stones) - 1:
            return True

        for i in range(pos + 1, len(stones)):
            gap = stones[i] - stones[pos]
            if jumpSize - 1 <= gap <= jumpSize + 1:
                if self.dfs(stones, i, gap):
                    return True
        return False

    # Memo verison, adding two D array
    # Time: O(n ^ 3)
    # Space: O(n ^ 2)
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        memo = [[-1] * n for _ in range(n)]
        return self.dfs(stones, 0, 0, memo)

    # current pos, current jumpSize
    def dfs(self, stones, pos, jumpSize, memo):
        if pos == len(stones) - 1:
            memo[pos][jumpSize] = 1
            return memo[pos][jumpSize]

        for i in range(pos + 1, len(stones)):
            gap = stones[i] - stones[pos]
            if jumpSize - 1 <= gap <= jumpSize + 1:
                if self.dfs(stones, i, gap, memo) == 1:
                    memo[pos][gap] = 1
                    return memo[pos][gap]
        memo[pos][jumpSize] = 0
        return memo[pos][jumpSize]

    # Memo version
    # Much Faster memo version.
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        stones = set(stones)
        memo = set()
        return self.backtrack(stones, 1, 1, target, memo)

    def backtrack(self, stones, pos, jumpSize, target, memo):
        if (pos, jumpSize) in memo:
            return False
        if pos == target:
            return True
        if jumpSize <= 0 or pos not in stones:
            return False

        for j in (jumpSize - 1, jumpSize, jumpSize + 1):
            if self.backtrack(stones, pos + j, j, target, memo):
                return True
        # memo only saves the failed jump at that pos
        memo.add((pos, jumpSize))
        return False
