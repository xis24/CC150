from typing import Optional


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class FlattenBinaryTreeToLinkedList:

    '''
    Given the root of a binary tree, flatten the tree into a "linked list":

    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.  
    '''

    def flatten(self, root: Optional[TreeNode]) -> None:
        self.dfs(root)

    def dfs(self, root):
        if not root:
            return root
        if not root.left and not root.right:
            return root

        leftTail = self.dfs(root.left)
        rightTail = self.dfs(root.right)

        if leftTail:
            leftTail.right = root.right
            root.right = root.left
            root.left = None
        return rightTail if rightTail else leftTail
