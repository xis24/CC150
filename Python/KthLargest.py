import heapq
from typing import List
import random


class KthLargest:

    # heap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        for i in range(k - 1):
            heapq.heappop(heap)
        return heap[0]

    # quick select

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.select(nums, 0, len(nums) - 1, len(nums) - k)

    def select(self, nums, left, right, k_smallest):
        if left == right:
            return nums[left]
        pivot_index = random.randint(left, right)
        pivot_index = self.partition(nums, left, right, pivot_index)

        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return self.select(nums, left, pivot_index - 1, k_smallest)
        else:
            return self.select(nums, pivot_index + 1, right, k_smallest)

    def partition(self, nums, left, right, pivot_index):
        pivot = nums[pivot_index]
        # move pivot to the end
        nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
        # move all smaller item to left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index
