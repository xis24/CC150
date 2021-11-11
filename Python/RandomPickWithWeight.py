from typing import List
import random


class RandomPickWithWeight:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        prefix_sum = 0

        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        for i, x in enumerate(self.prefix_sum):
            if target < x:
                return i

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()

        left = 0
        right = len(self.prefix_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if target > self.prefix_sum[mid]:
                left = mid + 1
            else:
                right = mid
        return left
