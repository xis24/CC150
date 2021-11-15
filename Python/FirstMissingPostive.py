from typing import List


class FirstMissingPostive:

    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while i < n:
            j = nums[i] - 1

            # put num[i] to the correct place if nums[i] in the range [1, n]
            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        # So far, all the integers that could find their own correct place
        # have been put to the correct place. next thing is to find out the place
        # that occupied wrongly
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == '__main__':
    obj = FirstMissingPostive()
    print(obj.firstMissingPositive([1, 2, 0]))
    print(obj.firstMissingPositive([3, 4, -1, 1]))
    print(obj.firstMissingPositive([7, 8, 9, 11, 12]))
