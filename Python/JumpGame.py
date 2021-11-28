from enum import Enum
from typing import List
import collections


class JumpGame:

    '''
    This is a dynamic programming[1] question. Usually, solving and fully understanding a dynamic programming problem is a 4 step process:

    Start with the recursive backtracking solution
    Optimize by using a memoization table (top-down[2] dynamic programming)
    Remove the need for recursion (bottom-up dynamic programming)
    Apply final tricks to reduce the time / memory complexity

    '''

    # pure brute force, and try all possible
    # Time: O(2 ^ n)
    # Space: O(n)
    def canJump(self, nums: List[int]) -> bool:
        return self.backtrack(0, nums)

    def backtrack(self, pos, nums):
        if pos == len(nums) - 1:
            return True

        furthestJump = min(pos + nums[pos], len(nums) - 1)
        for nextPosition in range(pos + 1, furthestJump + 1):
            if self.backtrack(nextPosition, nums):
                return True
        return False


class Status(Enum):
    Unknown = 1
    Bad = 2
    Good = 3

    # memo-ed version, top down version
    # O(n ^ 2)

    def canJump(self, nums: List[int]) -> bool:
        # 0 unknown 1 bad, 2 good
        memo = [Status.Unknown] * len(nums)
        memo[len(nums) - 1] = Status.Good

        return self.backtrack(0, nums, memo)

    def backtrack(self, pos, nums, memo):
        if memo[pos] != Status.Unknown:
            return True if memo[pos] == Status.Good else False

        furthestJump = min(pos + nums[pos], len(nums) - 1)
        for nextPos in range(pos + 1, furthestJump + 1):
            if self.backtrack(nextPos, nums, memo):
                memo[pos] = Status.Good
                return True
        memo[pos] = Status.Bad
        return False

    # bottom up version
    def canJump(self, nums: List[int]) -> bool:
        # 0 unknown 1 bad, 2 good
        memo = [Status.Unknown] * len(nums)
        memo[len(nums) - 1] = Status.Good

        for i in range(len(nums) - 2, -1, -1):
            furthestJump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthestJump + 1):
                if memo[j] == Status.Good:
                    memo[i] = Status.Good
                    break
        return memo[0] == Status.Good

    # optimal solution
    # time: O(n)
    # space: O(1)
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0

    '''
    jump game 2
    Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Your goal is to reach the last index in the minimum number of jumps.
    You can assume that you can always reach the last index.

    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
    '''

    def jump(self, nums: List[int]) -> int:
        memo = [1001] * len(nums)
        return self.jumpInternal(nums, memo, 0)

    def jumpInternal(self, nums, memo, pos):
        # when we reach the end, return 0 since no more jumps required
        if pos >= len(nums) - 1:
            return 0
        if memo[pos] != 1001:
            return memo[pos]

        for i in range(1, nums[pos] + 1):
            memo[pos] = min(
                memo[pos], 1 + self.jumpInternal(nums, memo, pos + i))
        return memo[pos]

    '''
    The idea is to maintain two pointers left and right, where left initialy set to be 0 and right set to be nums[0].
    So points between 0 and nums[0] are the ones you can reach by using just 1 jump.
    Next, we want to find points I can reach using 2 jumps, so our new left will be set equal to right, and our new right will be set equal to the farest point we can reach by two jumps. which is:
    right = max(i + nums[i] for i in range(left, right + 1)
    '''

    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        left, right = 0, nums[0]
        ret = 1
        while right < len(nums) - 1:
            ret += 1
            next = max(i + nums[i] for i in range(left, right + 1))
            left = right
            right = next
        return ret

    '''
    Jump Game iii

    Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
    Notice that you can not jump outside of the array at any time.
    '''

    # BFS O(n)
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = collections.deque([start])
        visited = [False] * n

        while queue:
            i = queue.popleft()
            if arr[i] == 0:
                return True
            if visited[i]:
                continue
            visited[i] = True
            if i - arr[i] >= 0:
                queue.append(i - arr[i])
            if i + arr[i] < n:
                queue.append(i + arr[i])
        return False

    # DFS
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)
        # using the start value from the problem
        return self.dfs(arr, visited, start)

    def dfs(self, arr, visited, start):
        if 0 <= start < len(arr) and not visited[start]:
            if arr[start] == 0:
                return True
            visited[start] = True
            return self.dfs(arr, visited, start + arr[start]) or self.dfs(arr, visited, start - arr[start])
        return False
