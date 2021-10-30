from heapq import heappop, heappush
from typing import List


class MinCostToConnectSticks:

    def connectSticks(self, sticks: List[int]) -> int:
        min_heap = []
        for num in sticks:
            heappush(min_heap, num)

        min_cost = 0
        while len(min_heap) > 1:
            cost = heappop(min_heap) + heappop(min_heap)
            min_cost += cost
            heappush(min_heap, cost)
        return min_cost


if __name__ == '__main__':
    obj = MinCostToConnectSticks()
    print(obj.connectSticks([2, 4, 3]))
    print(obj.connectSticks([1, 8, 3, 5]))
