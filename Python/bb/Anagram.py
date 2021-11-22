import collections
from typing import List


class Anagram:

    '''
    Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.
    Return the minimum number of steps to make t an anagram of s.
    An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.   

    '''

    def minSteps(self, s, t):
        s_count = collections.Counter(s)
        res = 0
        for char in t:
            if s_count[char] > 0:  # diff between s and t
                s_count[char] -= 1
            else:
                res += 1
        return res

    def groupAnagram(self, strs: List[List[str]]):
        word_to_anagram = collections.defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            word_to_anagram[tuple(count)].append(word)
        return word_to_anagram.values()


if __name__ == '__main__':
    obj = Anagram()
    print(obj.groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
