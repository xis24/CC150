import collections
import math
from typing import List


class MinWindowSubstring:
    # Given two string s and t, and t could have duplicate chars,
    # find out the min substirng in s such that every char in t is there
    # sliding window
    def minWindow(self, s: str, t: str) -> str:
        counterMap = collections.Counter(t)
        dictionCounter = len(counterMap)

        left = 0
        right = 0
        minLen = math.inf
        start = left  # start position of sequence
        while right < len(s):
            if s[right] in counterMap:
                counterMap[s[right]] -= 1
                if counterMap[s[right]] == 0:
                    dictionCounter -= 1

            while dictionCounter == 0:
                if s[left] in counterMap:
                    counterMap[s[left]] += 1
                    if counterMap[s[left]] > 0:
                        dictionCounter += 1

                    if right - left + 1 < minLen:
                        minLen = right - left + 1
                        start = left
                left += 1
            right += 1

        return "" if min == math.inf else s[start:start + minLen]


class SlindingWindowMax:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque([])
        ret = []

        for idx, num in enumerate(nums):
            while deque and nums[deque[-1]] < num:
                deque.pop()
            deque.append(idx)

            if deque[0] == idx - k:
                deque.popleft()

            if idx >= k - 1:
                ret.append(nums[deque[0]])
        return ret


class FindAllAnagramsInAString:

    # return the start index of anagram of p in S
    # Time: O(n)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sLen = len(s)
        pLen = len(p)
        if sLen < pLen:
            return []
        s_count = [0] * 26
        p_count = [0] * 26
        ret = []
        for char in p:
            p_count[ord(char) - ord('a')] += 1

        for i in range(sLen):
            s_count[ord(s[i]) - ord('a')] += 1
            # check the window size
            if i >= pLen:
                s_count[ord(s[i - pLen]) - ord('a')] -= 1
            if s_count == p_count:
                ret.append(i - pLen + 1)
        return ret


if __name__ == '__main__':
    obj = MinWindowSubstring()
    print(obj.minWindow('ADOBECODEBANC', 'ABC'))
    print(obj.minWindow('ACBBECODEBANC', 'ABBC'))
    print(obj.minWindow('BAOBBCABBC', 'ABBC'))
