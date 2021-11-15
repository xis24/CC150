from typing import Optional


'''
follow-u‍‌‍‌‍‍‍‌‌‌‍‍‍‍‍‍‌p:
1. 可不可以不在每个节点存subtree sum？
2. 如果把int改成float，会有什么影响？
3. 如果允许add/update/delete node，要怎样做？
'''


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return self.val


class EqualTreePartition:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        self.cuts = set()
        self.root = root
        result = self.getSum(root)
        print(self.cuts)

        return result / 2 in self.cuts

    def getSum(self, node):
        if not node:
            return 0
        totalSum = node.val + self.getSum(node.left) + self.getSum(node.right)
        if node is not self.root:
            self.cuts.add(totalSum)
        return totalSum


if __name__ == '__main__':
    obj = EqualTreePartition()
    node = TreeNode(5, TreeNode(10),
                    TreeNode(10, TreeNode(2), TreeNode(3)))

    nodeTrap = TreeNode(9, TreeNode(-1), TreeNode(1))
    print(obj.checkEqualTree(node))
    print(obj.checkEqualTree(nodeTrap))
