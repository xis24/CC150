from typing import List


class LongestIncreasingSubsequence:

    # Time complexity O(n^2)
    # Space complexity O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] represents the length of longest increasing subsequence that is ends
        # at ith element

        dp = [1] * len(nums)

        for j in range(len(nums)):
            for i in range(j):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)

    # Time complexity O(n^2)
    # Space complexity O(n)

    def lengthOfLIS(self, nums: List[int]) -> int:
        # build subsequence
        sub = nums[0]

        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # find the first element in sub that is greater than or equal to num
                i = 0
                while sub[i] < num:
                    i += 1
                sub[i] = num
        return len(sub)

    # Time complexity O(nlog(n))
    # Space complexity: O(n)

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for num in nums:
            i = self.findIndex(sub, num)

            # this means that all numbers in sub are smaller
            # thus the insertion point is at the at the array
            if i == len(sub):
                sub.append(num)
            else:  # this means there is a insert place in array
                sub[i] = num
        return len(sub)

    def findIndex(self, arr, num):
        start = 0
        end = len(arr) - 1
        index = len(arr)

        while start <= end:
            mid = (start + end) // 2
            if arr[mid] >= num:
                index = mid
                end = mid - 1
            else:
                start = mid + 1
        return index
