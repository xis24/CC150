from collections import heapq


class MaxStack:

    # O(n) solutuion to deal with popMax

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack and x >= self.stack[self.stack[-1][1]][0]:
            i = len(self.stack)
        else:
            i = self.stack[-1][1] if self.stack else 0
        self.stack.append((x, i))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[self.stack[-1][1]][0]

    # here we can also use another storage to make it easier too

    def popMax(self) -> int:
        index = self.stack[-1][1]  # index of current max
        result = self.stack[index][0]  # max value to return
        new_max = self.stack[self.stack[index-1]
                             [1]][0] if index > 0 else -float('inf')
        # Scan the stack starting at 'index' to recompute the max values and shift all
        # values to the left by one:
        for i in range(index, len(self.stack) - 1):
            if self.stack[i + 1][0] >= new_max:
                new_max = self.stack[i + 1][0]
                self.stack[i] = (new_max, i)
            else:
                self.stack[i] = (self.stack[i + 1][0], self.stack[i - 1][1])
        self.stack.pop()
        return result


# Follow up: Could you come up with a solution
# that supports O(1) for each top call
# and O(logn) for each other call?

    def __init__(self):
        self.soft_deleted = set()
        self.max_heap = []
        self.stack = []
        self.next_id = 0

    def push(self, x):
        heapq.heappush(self.max_heap, (-x, self.next_id))
        self.stack.append((x, self.next_id))
        self.next_id -= 1

    def pop(self):
        ret = self.stack.pop()
        self.soft_deleted.add(ret[1])
        self._clean_up()
        return ret[0]

    def top(self):
        return self.stack[-1][0]

    def peekMax(self):
        return -self.max_heap[0][0]

    def popMax(self):
        value, cur_id = heapq.heappop(self.max_heap)
        self.soft_deleted.add(cur_id)
        self._clean_up()
        return value

    def _clean_up(self):
        while self.stack and self.stack[-1][1] in self.soft_deleted:
            self.soft_deleted.remove(self.stack.pop()[1])
        while self.max_heap and self.max_heap[0][1] in self.soft_deleted:
            self.soft_deleted.remove(heapq.heappop(self.max_heap)[1])
