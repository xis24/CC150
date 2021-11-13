import collections
import math


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


if __name__ == '__main__':
    obj = MinWindowSubstring()
    print(obj.minWindow('ADOBECODEBANC', 'ABC'))
    print(obj.minWindow('ACBBECODEBANC', 'ABBC'))
    print(obj.minWindow('BAOBBCABBC', 'ABBC'))
