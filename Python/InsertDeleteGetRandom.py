import random
import collections


class InsertDeleteGetRandom:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            idx = self.dict[val]  # where orignal value idx in list
            lastElement = self.list[-1]  # current last position
            self.dict[lastElement] = idx
            self.list[idx] = lastElement
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)

    # If we allow duplicate

    def __init__(self):
        self.index = collections.defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        self.index[val].add(len(self.list))
        self.list.append(val)
        return len(self.index[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.index[val]:
            return False
        remove = self.index[val].pop()
        lastElement = self.list[-1]
        self.list[remove] = lastElement
        self.index[lastElement].add(remove)
        self.index[lastElement].discard(len(self.list) - 1)
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)
