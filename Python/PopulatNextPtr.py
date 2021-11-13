import collections


class Node:
    def __init__(self, val, left, right, next) -> None:
        self.val = val
        self.left = left
        self.right = right
        self. next = next


class PopulatNextRightPtr:

    # BFS solution
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        queue = collections.deque([root])
        while queue:
            size = len(queue)

            for i in range(size):
                front = queue.popleft()

                # make sure we are connecting to right node on the same leve
                if i < size - 1:
                    front.next = queue[0]
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
        return root

    # Recursive
    # Time complexity O(n)
    # Space complexity O(1) without count stack space

    def connect(self, root: Node) -> Node:
        self.dfs(root, None)

    def dfs(self, cur, nextptr):
        if not cur:
            return
        # connect the pointer first
        cur.next = nextptr
        self.dfs(cur.left, cur.right)
        if cur.next:
            self.dfs(cur.right, cur.next.left)
        else:
            self.dfs(cur.right, cur.next)

    # iternative

    def connect(self, root: Node) -> Node:
        if not root:
            return root

        leftMost = root

        while leftMost.left:
            head = leftMost
            # Treat as a linkedlist
            #
            while head:
                # left pointer
                head.left.next = head.right

                # connect right pointer if needed
                if head.next:
                    head.right.next = head.next.left
                # move pointer to next node
                head = head.next
            leftMost = leftMost.left
        return root
