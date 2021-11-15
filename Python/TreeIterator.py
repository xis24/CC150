import collections
from typing import Optional


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = collections.deque([])
        self.list = []
        self.pushLeft(root)
        self.pos = -1  # denote current position of element

    def next(self) -> int:
        self.pos += 1
        # this guards us to not pushleft for same elements
        if self.pos == len(self.list):
            top = self.stack.pop()
            self.list.append(top.val)
            self.pushLeft(top.right)
        return self.list[self.pos]

    def hasNext(self) -> bool:
        return self.stack or self.pos + 1 < len(self.list)

    def prev(self) -> int:
        self.pos -= 1
        return self.list[self.pos]

    def hasPrev(self) -> bool:
        return self.pos > 0

    def pushLeft(self, node):
        cur = node
        while cur:
            self.stack.append(cur)
            cur = cur.left
