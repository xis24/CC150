from typing import Optional
import math


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxAverageSubstree:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_avg = -math.inf
        self.dfs(root)
        return self.max_avg

    def dfs(self, root):
        if not root:
            return (0, 0)
        sum_left_node, total_count_left = self.dfs(root.left)
        sum_right_node, total_count_right = self.dfs(root.right)

        total_sum = root.val + sum_left_node + sum_right_node
        total_count = 1 + total_count_left + total_count_right

        avg = total_sum / total_count

        if avg > self.max_avg:
            self.max_avg = avg
        return (total_sum, total_count)
