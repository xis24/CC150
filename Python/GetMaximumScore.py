from typing import List


class GetMaximumScore:

    '''
    Logic is simple:
    Let's say that a place where nums1[i] = nums2[j] is checkpoint.
    Then result will be max prefix sum of two arrays + checkpoint + max sum postfix of two arrays
    Or: max(sum(nums1[0:i]), sum(nums2[0:j]) + checkpoint + max(sum(nums1[i + 1:]), sum(nums2[j + 1:]))

    So what we need to do is:

    Iterate through two arrays with calculating sum until we find checkpoint
    Add larger sum to result.
    Add checkpoint to result.
    Reset sums.
    Repeat.
    '''


def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
    sum1 = 0
    sum2 = 0
    ret = 0
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            sum1 += nums1[i]
            i += 1
        elif nums1[i] > nums2[j]:
            sum2 += nums2[j]
            j += 1
        else:
            ret += max(sum1, sum2) + nums1[i]
            sum1 = 0
            sum2 = 0
            i += 1
            j += 1
    while i < len(nums1):
        sum1 += nums1[i]
        i += 1

    while j < len(nums2):
        sum2 += nums2[j]
        j += 1
    return (ret + max(sum1, sum2)) % (10**9 + 7)
