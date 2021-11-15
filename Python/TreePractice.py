class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.value)


class Traversal:

    def postorder(self, root):
        if not root:
            return root
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        print("mid", root)

        if not left and not right:
            print("both node are empty")
            return None

        if left and right:
            print("prev return", root)
            return root

        node = left if left else right
        print("last return", node)
        return node


if __name__ == '__main__':
    node = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2))

    obj = Traversal()
    obj.postorder(node)
