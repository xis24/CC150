from typing import List, Optional
import collections
import math


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class PathSum:
    # check if current tree has this sum
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    # output all ROOT-LEAF path

    # Time complexity O(n^2), for every left we performing O(n) copy
    # Sapce complexity O(n) not counting output space
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        pathList = []
        self.dfs(root, targetSum, [], pathList)
        return pathList

    def dfs(self, root, remainingSum, listNodes, pathList):
        if not root:
            return
        listNodes.append(root.val)
        if not root.left and not root.right and remainingSum == root.val:
            pathList.append(list(listNodes))
        else:
            self.dfs(root.left, remainingSum - root.val, listNodes, pathList)
            self.dfs(root.right, remainingSum - root.val, listNodes, pathList)
        listNodes.pop()  # backtrack step

    # output the number of pathSums from parent to chilren, not necessarily from root to leaf

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ret = 0
        self.targetSum = targetSum
        self.hashmap = collections.defaultdict(int)
        self.preorder(root, 0)
        return self.ret

    def preorder(self, node, curSum):
        if not node:
            return
        curSum += node.val  # current prefix sum

        if curSum == self.targetSum:  # found one solution
            self.ret += 1

        # count that curSum - targetSum already occurred, this result the number of tiems a path with targetSum up to this current node
        self.ret += self.hashmap[curSum - self.targetSum]

        self.hashmap[curSum] += 1  # increament curSum count

        self.preorder(node.left, curSum)
        self.preorder(node.right, curSum)

        # important steps!
        # remove the curSum from the hashmap to avoid using it during the parallel substree processing
        self.hashmap[curSum] -= 1

    '''
    Path Sum IV

    If the depth of a tree is smaller than 5, then this tree can be represented by an array of three-digit integers. For each integer in this array:

    The hundreds digit represents the depth d of this node where 1 <= d <= 4.
    The tens digit represents the position p of this node in the level it belongs to where 1 <= p <= 8. The position is the same as that in a full binary tree.
    The units digit represents the value v of this node where 0 <= v <= 9.
    
    '''
    # solution 1: we could construct the tree and then apply path sum one
    # solution 2, we notice that the representation of tree is special, meaning 123, depth 1, pos 2, where 12 is unique ID, we can map this ID to its value.
    # the we can traverse the tree

    def pathSum(self, nums: List[int]) -> int:
        # generate map
        self.hashmap = {num // 10: num % 10 for num in nums}
        root = nums[0] // 10
        self.ret = 0
        self.dfs(root, 0)
        return self.ret

    # node is the ID of tree node
    def dfs(self, node, curSum):
        if node not in self.hashmap:
            return
        curSum += self.hashmap[node]
        depth, pos = divmod(node, 10)  # depth and position of current node
        left = (depth + 1) * 10 + 2 * pos - 1
        right = left + 1

        if left not in self.hashmap and right not in self.hashmap:
            self.ret += curSum
        else:
            self.dfs(left, curSum)
            self.dfs(right, curSum)

    '''
    129. Sum Root to Leaf Numbers
    You are given the root of a binary tree containing digits from 0 to 9 only.
    Each root-to-leaf path in the tree represents a number.
    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
    Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
    A leaf node is a node with no children.
    '''

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        self.dfs(root, 0)
        return self.ret

    def dfs(self, root, curSum):
        if not root:
            return
        curSum += curSum * 10 + root.val
        if not root.left and not root.right:
            self.ret += curSum
        else:
            self.dfs(root.left, curSum)
            self.dfs(root.right, curSum)

    '''
    Binary Tree Maximum Path Sum
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
    The path sum of a path is the sum of the node's values in the path.
    Given the root of a binary tree, return the maximum path sum of any non-empty path.
    '''
    # Note that there could be negative numbers, we definitely want to use max(xx, 0) to guard against situation
    # Time complexity: O(n)
    # Space complexity: O(h) where h is the height of tree, if tree is skewed (not balanced), it's O(n)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ret = -math.inf
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root:
            return 0
        left = max(self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)

        self.ret = max(self.ret, left + right + root.val)
        return max(left, right) + root.val

    '''
    988. Smallest String Starting From Leaf
    You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.
    Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
    As a reminder, any shorter prefix of a string is lexicographically smaller.
    For example, "ab" is lexicographically smaller than "aba".
    A leaf of a node is a node that has no children.
    '''

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ret = '~'  # initilize a char which has larger value than letters
        self.dfs(root, [])
        return self.ret

    def dfs(self, root, tempList):
        if not root:
            return
        tempList.append(chr(root.val + ord('a')))
        if not root.left and not root.right:
            self.ret = min(self.ret, "".join(reversed(tempList)))
        self.dfs(root.left, tempList)
        self.dfs(root.right, tempList)
        tempList.pop()  # backtrack step
