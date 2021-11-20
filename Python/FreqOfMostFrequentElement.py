from typing import List


class FreqOfMostFrequentElement:

    '''
    The frequency of an element is the number of times it occurs in an array.
    You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
    Return the maximum possible frequency of an element after performing at most k operations.
    '''

    def maxFrequency(self, nums: List[int], k: int) -> int:
        left = 0
        ret = 1  # min value
        curSum = 0
        for right in range(len(nums)):
            curSum += nums[right]

            # we want to find out the valid condition curSum + k >= nums[right] * (right - left +1)
            # so when the while condition stops, it's the condition.
            while curSum + k < nums[right] * (right - left + 1):
                curSum -= nums[left]
                left += 1
            ret = max(right - left + 1, ret)

        return ret
