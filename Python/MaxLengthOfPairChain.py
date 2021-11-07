from typing import List
import math


class MaxLengthOfPairChain:

    # if a chain of length k ends at some pairs[i],
    # and pairs[i][1] < pairs[j][0], we can extend this chain
    # to chain of length k + 1
    # 1. sort it first
    # 2. double for loop to compare

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)

    # pairA appears before pairB
    # => pairA[1] < pairB[1]
    # => claim: it's always better to add pairA first

    # two situation,
    # 1. when pairA[1] < pairB[0], it's always better to add pairA first
    # 2. when pairA[1] >= pairB[0], we need either append either append A or B
    #  => append either will increase the length by 1
    # However, (cur is the tail of chain)
    # appending pairA will have cur = pairA[1]
    # appending pairB will have cur = pairB[1]
    # AND pairA[1] < pairB[1]
    # we shall append pairA because smaller tail which has a better change to append more
    # pairs in the future

    # Time complexiy: O(nlogn)
    # Space complexity: O(n)
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        N = len(pairs)
        pairs.sort(key=lambda x: x[1])
        ans = 0
        cur = -math.inf

        for head, tail in pairs:
            if head > cur:
                ans += 1
                cur = tail
        return ans
