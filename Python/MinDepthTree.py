from typing import Optional
import math


class TreeNode:
    def __init__(self) -> None:
        pass


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class MinDepthTree:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        min_height = math.inf
        if root.left:
            min_height = min(min_height, self.minDepth(root.left))

        if root.right:
            min_height = min(min_height, self.minDepth(root.right))

        return min_height + 1


class MaxDepthTree:
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


class MaxDepthOfNaryTree:
    def maxDepth(self, root: 'Node') -> int:
        self.max_height = 0
        self.dfs(root, 0)
        return self.max_height

    def dfs(self, root, depth):
        if not root:
            return 0
        self.max = max(self.max, depth + 1)
        for child in root.children:
            self.dfs(child, depth + 1)


class MinHeightTrees:
    def minHeightTrees(self, n, edges):
        if n <= 2:
            return [i for i, _ in edges]
        graph = [set() for i in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [i for i in range(n) if len(graph[i]) == 1]
        remaining_nodes = n

        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove current leaves along with edges
            while leaves:
                leaf = leaves.pop()
                neighbor = graph[leaf].pop()  # node connect to leaf
                # remove the leaf connection as well
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves  # in the end, at most 2 leaves will be left out
