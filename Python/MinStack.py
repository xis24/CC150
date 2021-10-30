class MinStack:

    # with one stack to store a pair
    # drawbacks is that min value might repetitive

    # Time complexity O(1)
    # Space complexity O(n)
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(current_min, val)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

    # try to solve the repetitve min number (in the first solution)
    # same time and space complexity, but use two stacks
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

    # if we always push the minimum number, we could also save a pair, [min, count]
    # note that tuple in Python is immutable and we need to save as []

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val < self.minStack[-1][0]:
            self.minStack.append([val, 1])
        elif val == self.minStack[-1][0]:
            self.minStack[-1][1] += 1

    def pop(self) -> None:
        if self.minStack[-1][0] == self.stack[-1]:
            self.minStack[-1][1] -= 1

        if self.minStack[-1][1] == 0:
            self.minStack.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1][0]
