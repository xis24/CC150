from typing import List, Optional
import math
import collections


class Node:
    def __init__(self, val, children: List[Node]):
        pass


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class ValidateBinarySearchTree:

    # Recursive i
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isBST = True
        self.prev = -math.inf
        self.dfs(root)
        return self.isBST

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if root.val >= self.prev:
            self.isBST = False
            return
        self.prev = root
        self.dfs(root.right)

    # Recusive ii
    # almost same as one but with return type
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -math.inf
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return True
        if not self.dfs(root.left):
            return False
        if root.val <= self.prev:
            return False
        self.prev = root.val
        return self.dfs(root.right)

    # Recusive iii
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, math.inf, -math.inf)

    def isValid(self, root, curMax, curMin):
        if not root:
            return True
        if root.val <= curMin or root.val >= curMax:
            return False

        return self.isValid(root.left, root.val, curMin) and self.isValid(root.right, curMax, root.val)

    # trim BST based on range
    def trimBST(self, root, low, high):
        # condition on each level
        if not root:
            return root
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        # within range connections
        root.left = self.trimBST(root.left, low, high)
        root.high = self.trimBST(root.right, low, high)
        return root

    # Serilize/Deserialize a BST
    # there are optimization where we can encode number to a byte string, so if the constraint given us that the number will be between 10^4,
    # we can use 4 byte strings,

    # pre order serilization

    def serialize(self, root: TreeNode) -> str:
        ret = []
        self.preorder(root, ret)
        return ' '.join(ret)

    def preorder(self, node, ret):
        if node:
            ret.append(str(node.val))
            self.preorder(node.left, ret)
            self.preorder(node.right, ret)

    def deserialize(self, data: str) -> TreeNode:
        vals = collections.deque(int(val) for val in data.split())
        return self.buildTree(vals, -math.inf, math.inf)

    def buildTree(self, vals, minVal, maxVal):
        if vals and minVal < vals[0] < maxVal:
            front = vals.popleft()
            node = TreeNode(front)
            node.left = self.buildTree(vals, minVal, front)
            node.right = self.buildTree(vals, front, maxVal)
            return node

    # Serilize/Deserialize a BT
    # we could use preorder, but we need to record the empty node. Intead, let's use level order traversal
    def serialize(self, root):
        if not root:
            return ""
        queue = collections.deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if not node:
                res.append('#')
                continue
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ','.join(res)

    def deserialize(self, data):
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        index = 1
        while q:
            node = q.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        return root

    # Serilialize/Deserilize N-ary tree

    # pre order serilize
    def serialize(self, root):
        serial = []

        def preorder(node):
            if not node:
                return
            serial.append(str(node.val))
            for child in node.children:
                preorder(child)
            serial.append("#")
        preorder(root)
        return " ".join(serial)

    def deserialize(self, data):
        if not data:
            return None
        tokens = collections.deque(data.split())
        root = Node(int(tokens.popleft()), [])

        def dfs(node):
            if not tokens:
                return

            while tokens[0] != '#':
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                dfs(child)
            tokens.popleft()  # discard "#"
        dfs(root)
        return root

    # max average substree
    # Solution: for each node, we record the sum of substree, and count the number of nodes
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_avg = -math.inf
        self.dfs(root)
        return self.max_avg

    def dfs(self, root):
        if not root:
            return (0, 0)
        sum_left_tree, count_left_tree = self.dfs(root.left)
        sum_right_tree, count_right_tree = self.dfs(root.right)

        total_sum = sum_left_tree + sum_right_tree + root.val
        total_count = count_left_tree + count_right_tree + 1

        avg = total_sum / total_count
        if avg > self.max_avg:
            self.max_avg = avg

        return (total_sum, total_count)

    # All Nodes Distance K in binary tree
    # solution 1
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.markParent(root, None)
        queue = collections.deque([(target, 0)])
        seen = {target}

        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.parent):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d + 1))
        return []

    def markParent(self, root, parent):
        if root:
            root.parent = parent
            self.markParent(root.left, root)
            self.markParent(root.right, root)

    # solution 2:build graph
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        self.buildGraph(root, None, graph)

        queue = collections.deque([(target, 0)])
        seen = {}
        ans = []

        while queue:
            node, d = queue.popleft()
            if node in seen:
                continue
            seen.add(node)
            if d == k:
                ans.append(node.val)
            elif d < k:
                for nei in graph[node]:
                    queue.append((nei, d + 1))
        return ans

    def buildGraph(self, node, parent, graph):
        if node:
            if parent:
                graph[node].append(parent)
            if node.left:
                graph[node].append(node.left)
                self.buildGraph(node.left, node, graph)
            if node.right:
                graph[node].append(node.right)
                self.buildGraph(node.right, node, graph)


if __name__ == '__main__':
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    obj = ValidateBinarySearchTree()
    print(obj.isValidBST(root))

    # serilization
    print(obj.serialize(root))
