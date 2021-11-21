import collections
from typing import List
import math
import bisect


class IPOShareDistribution:
    '''

  A company registers an IPO on a website sellshares.com. 
  All the shares on this website are available for bidding for a particular time frame called the bidding window.
  At the end of the bidding window an auction logic is used to decide how many of the available shares go to which bidder until all the shares that are available have been allotted,
  or all the bidders have received the shares they bid for, whichever comes earlier.

  The bids arrive from the users in the form of <user Id, number of shares, bidding price, timestamp> until the bidding window is closed.

  The auction logic assigns shares to the bidders as follows: 
  1. The bidder with the highest price gets the number of shares they bid for
  2. If multiple bidders have bid at the same price, the bidders are assigned shares as follows:
       Each bidder in the same price group gets assigned one share each consecutively, with each bidder being arranged inside the group based on their timestamp.
       Once a bidder gets the number of shares they bid for, they will be removed from the above iterative process and the process
       which then continues until all bidders are removed or the shares get exhausted, whichever comes first. 

  List the user Id's of all users who did not get even one share after the shares have been allocated. 

    '''

    def unsuccessfulBider(self, ipos, total_shares):
        ipos.sort(key=lambda bid: (-bid[2], bid[3]))

        price_to_bid = collections.OrderedDict()
        for bid in ipos:
            price_to_bid.setdefault(bid[2], []).append(bid)

        print(price_to_bid)

        ret = []

        for _, bids in price_to_bid.items():
            unfilled_id = []
            if total_shares <= 0:
                unfilled_id = map(lambda bid: bid[0], bids)
                ret.extend(unfilled_id)
            else:
                if total_shares >= len(bids):
                    share_list = map(lambda bid: bid[1], bids)
                    total_shares -= sum(share_list)
                else:
                    rest = bids[total_shares:]
                    unfilled_id = map(lambda bid: bid[0], rest)
                    ret.extend(unfilled_id)
        return ret

    def unsuccessfulBider2(self, ipos, total_shares):
        ipos.sort(key=lambda bid: (-bid[2], bid[3]))

        price_to_bid = collections.OrderedDict()
        for bid in ipos:
            price_to_bid.setdefault(bid[2], []).append(bid)

        ret = []
        for _, bids in price_to_bid.items():
            if total_shares >= len(bids):
                total_shares -= sum(map(lambda bid: bid[1], bids))
            elif 0 < total_shares < len(bids):
                rest = bids[total_shares:]
                for bid in rest:
                    bisect.insort(ret, bid[0])
                total_shares = 0
            else:
                for bid in bids:
                    bisect.insort(ret, bid[0])
        return ret

    '''
    下水道出水, Tree， 分成两个tree， 让出水量差最小
    inputs:
    parent: List(int): parent = j => j 是 i 的parent
    inputs: List(int): 每个node的额外出水量

    先construct nodes： nodes = [TreeNode(inputs) for i in range(len(parent)]
    然后用parents construct tree
    用DFS 算出每个节点的总出水量
    interate nodes, nodes[0]  是总出水量, node 是 i node 的总出‍‌‍‌‍‍‍‌‌‌‍‍‍‍‍‍‌水量，出水量差 = abs(nodes[0].flow - 2  node.flow)

    '''


class TreeNode:
    def __init__(self, val=0) -> None:
        self.val = val
        self.children = []
        self.total = 0


class DrainagePartition:

    def drainagePartiton(self, parent: List[int], inputs: List[int]):
        # build the tree
        # tree[i] = [j, k], where j and k is the children of i
        n = len(parent)
        tree = collections.defaultdict(list)
        for i in range(n):
            if parent[i] == -1:
                continue
            tree[parent[i]].append(i)

        # water sum of substree
        sumWater = [0] * n

        totalwater = self.dfs(sumWater, tree, inputs, 0)
        ans = math.inf

        for subTreeSum in sumWater:
            # cut down the branch, the amount of water one peieces is substree sum
            # the amount of water of another prices is total water - subTreeSum
            ans = min(ans, abs(totalwater - subTreeSum - subTreeSum))
        return ans

    def dfs(self, sumWater, tree, inputs, node):
        # leaf node
        if len(tree[node]) == 0:
            sumWater[node] = inputs[node]
            return sumWater[node]
        ans = inputs[node]
        for child in tree[node]:
            ans += self.dfs(sumWater, tree, inputs, child)
        sumWater[node] = ans
        return sumWater[node]
##########################

    def drainagePartiton2(self, parent: List[int], inputs: List[int]):
        # initialize the nodes
        nodes = [TreeNode(value) for value in inputs]

        #
        root = TreeNode()
        for i in range(len(parent)):
            if parent[i] == -1:
                head = nodes[i]
            else:
                nodes[parent[i]].children.append(nodes[i])

        self.dfs(root)

        ret = math.inf

        cur_level = [root]
        while cur_level:
            new_level = []
            for node in cur_level:
                new_level += node.children
                res = min(ret, abs(root.total - 2 * node.total))
            cur_level = new_level
        return ret

    # calculate the sum of each subtree

    def dfs(self, root):
        curSum = root.val
        if root.chidlren:
            for child in root.children:
                curSum += self.dfs(child)
        root.total = curSum
        return curSum


if __name__ == "__main__":
    # assume one user can only enter one bid
    # user_id, shares, prices, timestamp
    ipos = [[1, 2, 5, 0],
            [2, 1, 4, 2],
            [3, 5, 4, 6]]

    # IPO
    obj = IPOShareDistribution()
    print(obj.unsuccessfulBider(ipos, 3))
    print(obj.unsuccessfulBider2(ipos, 3))

    #
