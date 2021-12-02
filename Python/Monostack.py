from typing import List


class Monostack:

    '''
    The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
    You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
    For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
    Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
    '''

    def nextLargerElement(self, nums):
        stack = []
        hashmap = {}
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                top = stack.pop()
                hashmap[top] = num
            stack.append(idx)

        while stack:
            hashmap[stack.pop()] = -1
        ret = []
        for i in range(len(nums)):
            ret.append(hashmap[i])
        return ret

    # next greater element ii
    # circular array
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)  # initialize to -1 for all result

        for i in list(range(len(nums))) * 2:
            while stack and stack[-1] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)

        return res


class OnlineStockSpan:
    def __init__(self) -> None:
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res


class RemoveDuplicateLetters:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurance = {}
        for idx, char in enumerate(s):
            last_occurance[char] = idx

        # last occurance
        # {b:3, c:4, a:2 }
        #         0 1 2 3 4
        #         b c a b c
        #               ^
        # stack a b c
        #

        for idx, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and idx < last_occurance[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)
        return "".join(stack)


class ShortedArrayToRemoveToMakeSorted:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = 0
        n = len(arr)
        right = n - 1

        # check the last index of increasing from left
        while left < right and arr[left] <= arr[left + 1]:
            left += 1

        if left == right:
            return 0

        # check the last index of decreasing from right
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # worst case, we either remove all the elements from front or all the elements from back
        minLen = min(n - left - 1, right)
        j = right

        # try to optimize the solution, see if we can merge two separate array (without actually merging it)
        # [1 2 3 10]  and [2 3 5]
        # what's the following is doing,
        # [1], [2, 3, 5] to make an increasing sequence
        # [1, 2], [2, 3, 5]
        # [1, 2, 3], [3, 5]
        # [1, 2, 3, 10], []
        # we need to find the min length of subarray to remove to make this happen
        for i in range(left + 1):
            while j <= n - 1 and arr[i] > arr[j]:
                j += 1
            if j == n:
                break
            minLen = min(minLen, j - i - 1)
        return minLen


class SumOfSubarrayMinimums:
    '''
    Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

    '''

    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        ret = [0] * len(arr)
        stack = [0]

        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            ret[i] = ret[j] + (i - j) * arr[i]
            stack.append(i)
        return sum(stack) % (10**9 + 7)


class NextLargerElement:

    def getNextLargerElement(self, nums):
        ret = [0] * len(nums)
        stack = []

        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                top = stack.pop()
                ret[top] = nums[idx]
            stack.append(idx)
        return ret


class LargestRectangleHistogram:
    # Divide and conquer
    # Time: O(n log n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        def divide_conquer(heights, start, end):
            if start > end:
                return 0
            min_index = start
            for i in range(start, end + 1):
                if heights[min_index] > heights[i]:
                    min_index = i
            return max(
                heights[min_index] * (end - start + 1),
                divide_conquer(heights, start, min_index - 1),
                divide_conquer(heights, min_index + 1, end),
            )
        return divide_conquer(heights, 0, len(heights) - 1)

    # Time: O(N)
    #
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0

        for idx, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                currentHeight = h - heights[stack.pop()]
                width = idx - stack[-1] - 1
                max_area = max(max_area, currentHeight * width)

        # this actually calculates the area of min height during the traverse
        while stack[-1] != -1:
            currentHeight = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, currentHeight * width)
        return max_area


if __name__ == '__main__':
    # obj = Monostack()
    nums = [2, 3, 5, 1, 0, 7, 3]
    #       1  5  3  3  0  3  0
    # print(obj.nextLargerElement(nums))
    # print(obj.nextGreaterElements(nums))

    # obj2 = ShortedArrayToRemoveToMakeSorted()
    # print(obj2.findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]))
    # print(obj2.findLengthOfShortestSubarray([1, 2, 3]))

    obj3 = NextLargerElement()
    print(obj3.getNextLargerElement(nums))
