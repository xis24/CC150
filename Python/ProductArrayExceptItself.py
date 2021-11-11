from typing import List


class ProductArrayExceptItself:

    ''''Assume we have an arry ... x .... we want to calculate the product except itself at x
    Naive solution would be double for loop to calculate the product of all elements before x
    and the product of all the element after x, and then we stored in answer array.
    This will result a O(n^2), and O(1) space

    Improved solution, we can trade space to improve time complexity. So we can have two array:
    prefix product array, and suffix product array. And the final answer would be prefix[i] * 
    suffix[i]

    this will give time complexity O(n) and space complexity O(n)

    '''

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        ret = [0] * n

        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        suffix[n - 1] = 1
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            ret[i] = prefix[i] * suffix[i]

        return ret

    ''' We actually don't need extra two arrays to save both prefix and suffix.
    We can use answer array to do that.
    1. iterate left to right to calculate the prefix and save to answer array
    2. iterate right to left with a variable, right to calculate suffix, at the same time
    update the ans array
    3. return ret
    '''

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * n
        ret[0] = 1

        for i in range(1, n):
            ret[i] = ret[i - 1] * nums[i - 1]

        right = 1

        for i in range(n - 1, -1, -1):
            ret[i] *= right
            right *= nums[i]

        return ret
