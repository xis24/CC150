from collections import defaultdict, deque
from typing import List
import string


class WordLadder:

    # start from one side
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([beginWord, 1])
        visited = set()
        wordDict = self.construct_dict(wordList)
        while queue:
            word, step = queue.popleft()
            if word not in visited:
                visited.add(word)
                if word == endWord:
                    return step
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    neigh_words = wordDict.get(s, [])
                    for neigh in neigh_words:
                        if neigh not in visited:
                            queue.append((neigh, step + 1))

        return 0

    def construct_dict(self, word_list):
        dict = defaultdict(list)
        for word in word_list:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                dict[s].append(word)
        return dict

    # Start from both side

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        beginSet = set()
        endSet = set()
        beginSet.add(beginWord)
        endSet.add(endWord)

        level = 1
        while beginSet and endSet:
            if len(beginSet) > len(endSet):  # swap
                beginSet, endSet = endSet, beginSet
            newBeginSet = set()
            for word in beginSet:
                for neigh in self.neighbors(word):
                    if neigh in endSet:
                        return level + 1
                    if neigh in wordSet:
                        newBeginSet.add(neigh)
                        wordSet.remove(neigh)
            beginSet = newBeginSet
            level += 1
        return 0

    def neighbors(self, s):
        res = []
        for i in range(len(s)):
            for c in string.ascii_lowercase:
                word = s[:i] + c + s[i + 1:]
                res.append(word)
        return res

# word ladder ii
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if endWord not in wordList:
            return []
        L = len(beginWord)

        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        ans = []
        queue = deque()
        queue.append((beginWord, [beginWord]))
        visited = set([beginWord])

        while queue and not ans:
            length = len(queue)

            localVisited = set()

            for _ in range(length):
                word, path = queue.popleft()
                for i in range(L):
                    for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
                        if nextWord == endWord:
                            ans.append(path + [endWord])
                        if nextWord not in visited:
                            localVisited.add(nextWord)
                            queue.append((nextWord, path + [nextWord]))
            visited = visited.union(localVisited)
        return ans
