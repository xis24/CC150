import math
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right


class VerticalOrderTraversal:

    # O(nlog(n)) solution
    # with global sorting
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_list = []

        # 1. constructor the node list with coordinates
        self.dfs(root, 0, 0, node_list)
        # 2. sort the node list globally, according to the coordinates
        node_list.sort()
        # 3. retrieve the sorted results grouped by the column index
        ret = []
        cur_column_index = node_list[0][0]
        cur_column = []

        for column, row, value in node_list:
            if column == cur_column_index:
                cur_column.append(value)
            else:
                # end of a column, start the next column
                ret.append(cur_column)
                cur_column_index = column
                cur_column = [value]
        ret.append(cur_column)  # append the last one

        return ret

    def dfs(self, root, row, column, node_list):
        if not root:
            return
        node_list.append((column, row, root.val))
        self.dfs(root.left, row + 1, column - 1, node_list)
        self.dfs(root.right, row + 1, column + 1, node_list)

    # local sorting (sort based on the column index)
    # O(nlog (n / k)) where k is the width of tree
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        self.min_column_index = math.inf
        self.max_column_index = -math.inf
        self.column_index = collections.defaultdict(list)
        self.dfs(root, 0, 0)

        ret = []
        for column in range(self.min_column_index, self.max_column_index + 1):
            ret.append([val for row, val in sorted(self.column_index[column])])
        return ret

    def dfs(self, root, row, col):
        if not root:
            return root
        self.column_index[col].append(row, root.val)
        self.min_column_index = min(self.min_column_index, col)
        self.max_column_index = max(self.max_column_index, col)
        self.dfs(root.left, row + 1, col - 1)
        self.dfs(root.right, row + 1, col + 1)
