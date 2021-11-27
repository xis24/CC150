import collections


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class SubArraySum:
    def subArraySum(self, nums, target):
        curSum = 0
        ret = 0
        hashmap = collections.defaultdict(int)
        for num in nums:
            curSum += num

            if target == curSum:
                ret += 1

            ret += hashmap[curSum - target]
            hashmap[curSum] += 1
        return ret


class PathSum3:

    def pathSum(self, root, targetSum):
        if not root:
            return root
        self.sum_map = collections.defaultdict(int)
        self.ret = 0
        self.dfs(root, 0, targetSum)
        return self.ret

    def dfs(self, root, curSum, targetSum):
        if not root:
            return
        curSum += root.val
        if curSum == targetSum:
            self.ret += 1
        self.ret += self.sum_map[curSum - targetSum]
        self.sum_map[curSum] += 1
        self.dfs(root.left, curSum, targetSum)
        self.dfs(root.right, curSum, targetSum)
        self.sum_map[curSum] -= 1


if __name__ == '__main__':
    obj = SubArraySum()
    print(obj.subArraySum([2, 3, 4, 3, 4, 2, 5], 7))
