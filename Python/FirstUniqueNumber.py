from typing import List, OrderedDict
from collections import deque


# contructor O(k), k is number of nums at the first
# showFirstUnique amortized O(1)
#  because the number of O(1) removals is proportiaonal to the numerb of aclls
#  to add(), we say that it's amortized O(1)
# add o(1)

class FirstUniqueNumber:

    def __init__(self, nums: List[int]) -> None:
        self._queue = deque()
        self._isUnique = {}
        for num in nums:
            self.add(num)

    def add(self, value: int) -> None:
        if value not in self._isUnique:
            self._isUnique[value] = True
            self._queue.append(value)
        else:
            self._isUnique[value] = False

    def showFirstUnique(self) -> int:
        while self._queue and not self._isUnique[self._queue[0]]:
            self._queue.popleft()
        if self._queue:
            return self._queue[0]
        return -1

    # O(1) operations by using OrderedDict
    # basically ordered dictionary

    def __init__(self, nums: List[int]):
        self._queue = OrderedDict()
        self._isUnique = {}
        for num in nums:
            self.add(num)

    def add(self, value: int) -> None:
        if value not in self._isUnique:
            self._isUnique[value] = True
            self._queue[value] = None
        elif self._isUnique[value]:
            self._isUnique[value] = False
            del self._queue[value]

    def showFirstUnique(self) -> int:
        if self._queue:
            return next(iter(self._queue))
        return -1
