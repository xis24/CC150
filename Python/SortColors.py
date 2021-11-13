from typing import List


class SortColors:

    # 1. discuss the approach
    # 2. run the test case
    # 3. ask if I can start to code
    # 4. start to code
    # 5. run test case with code
    # 6. time complexity and space complexity

    def sortColors(self, nums: List[int]) -> None:
        zeros = 0  # position next zero should be
        twos = len(nums) - 1  # posisiton next two should be
        cur = 0  # current position

        while cur <= twos:
            if nums[cur] == 2:
                nums[cur], nums[twos] = nums[twos], nums[cur]
                twos -= 1
            elif nums[cur] == 0:
                nums[cur], nums[zeros] = nums[zeros], nums[cur]
                zeros += 1
                cur += 1
            else:
                cur += 1

        return nums


if __name__ == '__main__':
    obj = SortColors()
    print(obj.sortColors([2, 1, 0, 2]))
    print(obj.sortColors([2, 2, 1, 2]))
