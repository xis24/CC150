from typing import List


class NestedInteger:
    def isInteger(self) -> bool:
        pass

    def getInteger(self) -> int:
        pass

    def getList(self) -> List[NestedInteger]:
        pass


class FlattenNestedListIterator:

    #
    # O(N + L)
    def __init__(self, nestedList: List[NestedInteger]):
        def flatten(nested_list):
            for nested_integer in nested_list:
                if nested_integer.isInteger():
                    self.integers.append(nested_integer.getIntger())
                else:
                    flatten(nested_integer.getList())
            self._integers = []
            self._pos = -1
            flatten(nestedList)

    def next(self) -> int:
        self.pos += 1
        return self._integers[self.pos]

    def hasNext(self) -> bool:
        return self.pos + 1 < len(self._integers)

    # less work is done in the constructor, and using iterator for the rest
    # Time O(1)
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = [[nestedList, 0]]

    def next(self) -> int:
        # if we assume operation is always valid. It's not necessary to do this step
        # self.hasNext
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()

    def hasNext(self) -> bool:
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._next = iterator.next()
        self._iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next

    def next(self):
        """
        :rtype: int
        """
        if not self._next:
            raise StopIteration()
        ret = self._next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self._next
