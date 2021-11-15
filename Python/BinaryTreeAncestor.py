from typing import List, Optional


class Node:
    def __init__(self, val, left=None, right=None, parent=None) -> None:
        self.val = val


class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.value)


class BinaryTreeAncestor:

    '''
    Lowest common ancestor in BINARY SEARCH TREE
    Since binary search tree has the property that all nodes on the left of root is smaller than root and all right nodes on
    the right will be greater than root, there could be three situation
    1. both p and q are on the right side of root, ancestor is on the right
    2. both p and q are on the left side of root, ancestor is on the left
    3. root is the ancessotr
    '''

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentVal = root.value
        pVal = p.value
        qVal = q.value

        if pVal < parentVal and qVal < parentVal:
            return self.lowestCommonAncestor(root.left, p, q)
        elif pVal > parentVal and qVal > parentVal:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    '''
    ancestor 1
    GIVEN BOTH P AND Q EXIST IN TREE !!!
    Lowest common ancestor in BINARY TREE
    
    '''

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root

        # one of node is foud, return root directly
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # can't find both node on the left and right, return None
        if not left and not right:
            return None
        # find both left and right, direclt return root
        if left and right:
            return root

        return left if left else right

    '''
    ancestor 2
    P and Q MIGHT NOT EXIST

    1. We need to know if both nodes exists in the tree
    2. If both nodes exist, we can return, otherwise return null
    '''

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.foundP = False
        self.foundQ = False
        lca = self.dfs(root, p, q)
        return lca if self.foundP and self.foundQ else None

    def dfs(self, root, p, q):
        if not root:
            return root
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if root == p:  # mark found p
            self.foundP = True
            return root
        if root == q:  # mark found q
            self.foundQ = True
            return root
        if left and right:  # we found it from both side, return ancestor
            return root
        return left if left else right  # return current node

    '''
    ancestor 3, 
    P and Q exist, and we have a parent pointer in each treeNode

    1. Since we have a parent pointer already, we can use this parent pointer to climb up the tree and record the path in a 
    set.
    2. then start from another node, and check if the path contains another node, if yes. We just return it
    3. Since we are guaranteed that both nodes will be in the tree
    '''

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_path_to_root = self.getPath(p)
        while q.parent:
            if q in p_path_to_root:
                return q
            q = q.parent
        return q

    def getPath(self, node):
        path = set()
        while node:
            path.add(node)
            node = node.parent
        return path

    # space: O(1) solution. It's SAME as finding the intersection of two linked list
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_head = p
        q_head = q

        while p_head != q_head:
            p_head = p_head.parent if p_head.parent else q
            q_head = q_head.parent if q_head.parent else p

        return p_head

    '''
    ancestor 4
    We want to find the ancestor of ALL NODES, all nodes exist in the tree 

    Time: O(n)
    Space: O(m)
    '''

    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        hashset = set(nodes)
        return self.dfs(root, hashset)

    def dfs(self, root, hashset):
        if not root:
            return root

        if root in hashset:
            return root

        left = self.dfs(root.left, hashset)
        right = self.dfs(root.right, hashset)

        if not left and not right:
            return None

        if left and right:
            return root

        return left if left else right

    '''
    Maximum Difference Between Node and Ancestor
    
    Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where 
    v = |a.val - b.val| and a is an ancestor of b.
    
    We can observe that if node has a ancestor, then they must be on the same path
    Thus, we can record min, max along the way, CACULATE THE DIFF at leaf
    '''

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root.val, root.val)

    def dfs(self, root, curMin, curMax):
        if not root:
            return abs(curMin - curMax)
        curMin = min(curMin, root.val)  # get current min
        curMax = max(curMax, root.val)  # get current max

        left = self.dfs(root.left, curMin, curMax)
        right = self.dfs(root.right, curMin, curMax)

        return max(left, right)  # return current max value at this point

    '''
    865. Smallest Subtree with all the Deepest Nodes

    Given the root of a binary tree, the depth of each node is the shortest distance to the root.
    Return the smallest subtree such that it contains all the deepest nodes in the original tree.
    A node is called the deepest if it has the largest depth possible among any node in the entire tree.

    The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.


    Intuition:
    1) First find the depthest depth
    2) find both left and right node have that depth
    3) return the node
    for the step 1 and 2, we can do it together while travesing
    '''

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.deepest = 0
        self.ret = None
        self.dfs(root, 0)
        return self.ret

    def dfs(self, root, curLevel):
        if not root:
            return curLevel
        left = self.dfs(root.left, curLevel + 1)
        right = self.dfs(root.right, curLevel + 1)

        curMax = max(left, right)
        self.deepest = max(self.deepest, curMax)
        if left == self.deepest and right == self.deepest:
            self.ret = root
        return curMax


if __name__ == '__main__':
    p = TreeNode(5, TreeNode(6), TreeNode(
        2, TreeNode(7), TreeNode(4)))
    q = TreeNode(1, TreeNode(0), TreeNode(8))
    root = TreeNode(3, p, q)
    obj = BinaryTreeAncestor()
    print(obj.lowestCommonAncestor(root, p, q))
