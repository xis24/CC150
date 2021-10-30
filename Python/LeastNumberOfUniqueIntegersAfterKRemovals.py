from typing import List
from collections import Counter
import heapq


class LeastNumberOfUniqueIntegersAfterKRemovals:

    # time complexity O(nlog(n))
    # space O(n)
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        min_heap = []  # stores min freq with key

        for key, freq in count.items():
            heapq.heappush(min_heap, (freq, key))

        while min_heap and k - min_heap[0][0] >= 0:
            k -= heapq.heappop(min_heap)[0]

        return len(min_heap)

    def findLeastNumOfUniqueInts2(self, arr, k):
        count = Counter(arr)
        occuranceCount = Counter(count.values())
        remaining = len(count)

        for key in range(1, len(arr) + 1):
            if k >= key * occuranceCount[key]:
                k -= key * occuranceCount[key]
                remaining -= occuranceCount[key]
            else:
                return remaining - k // key
        return remaining


if __name__ == '__main__':
    obj = LeastNumberOfUniqueIntegersAfterKRemovals()
    print(obj.findLeastNumOfUniqueInts([5, 5, 4], 1))
    print(obj.findLeastNumOfUniqueInts([5, 5, 3, 4, 3, 1], 2))
