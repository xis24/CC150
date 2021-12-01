from typing import List


class QuickSelect:

    def quickSelect(self, nums, k):
        self._quickSelect(nums, 0, len(nums) - 1, k)
        print(nums[len(nums) - k])
        return nums[:k]

    def _quickSelect(self, nums, left, right, k):
        if left < right:
            p = self.partition(nums, left, right)
            if p == k:
                return
            elif p < k:
                return self._quickSelect(nums, p + 1, right, k)
            else:
                return self._quickSelect(nums, left, p - 1, k)

    def partition(self, nums, left, right):
        pivot = nums[right]
        index = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        nums[index], nums[right] = nums[right], nums[index]
        return index

    # quick sort
    def quickSort(self, nums):
        self._quickSort(nums, 0, len(nums) - 1)
        return nums

    def _quickSort(self, nums, left, right):
        if left >= right:
            return
        pivot = self.partition(nums, left, right)

        self._quickSort(nums, left, pivot - 1)
        self._quickSort(nums, pivot + 1, right)

    # merge sort
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        first = nums[:mid]
        second = nums[mid:]
        newFirst = self.mergeSort(first)
        newSecond = self.mergeSort(second)
        newList = self.merge(newFirst, newSecond)
        return newList

    def merge(self, a, b):
        index_a = 0
        index_b = 0
        ret = []
        while index_a < len(a) and index_b < len(b):
            if a[index_a] <= b[index_b]:
                ret.append(a[index_a])
                index_a += 1
            else:
                ret.append(b[index_b])
                index_b += 1
        if index_a < len(a):
            for i in range(index_a, len(a)):
                ret.append(a[index_a])
        else:
            for i in range(index_b, len(b)):
                ret.append(b[index_b])
        return ret

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickselect(nums, 0, len(nums) - 1, k)

    def quickselect(self, nums, left, right, k):
        p = self.partition(nums, left, right)
        if p == k - 1:
            return nums[p]
        elif p < k:
            return self.quickselect(nums, p + 1, right, k)
        else:
            return self.quickselect(nums, left, p - 1, k)

    def partition(self, nums, left, right):
        pivot = nums[right]
        index = left

        for i in range(left, right):
            if nums[i] > pivot:
                nums[index], nums[i] = nums[i],  nums[index]
                index += 1

        nums[index], nums[right] = nums[right], nums[index]
        return index


if __name__ == '__main__':
    obj = QuickSelect()
    # print(obj.quickSelect([7, 4, 6, 3, 9, 1], 2))
    # print(obj.quickSort([7, 4, 6, 3, 9, 1]))
    # print(obj.mergeSort([7, 4, 6, 3, 9, 1]))
    print(obj.findKthLargest([3, 2, 1, 5, 6, 4], 2))
