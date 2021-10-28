from collections import deque
from functools import lru_cache


class WordBreak:
    # Word Break i
    # DP solution
    # Time complexity: O(n^3)
    def wordBreakDP(self, s, wordDict):
        if not wordDict:
            return False
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True  # null string is always present in the dict
        wordDict = set(wordDict)

        for i in range(n):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[n]

    # BFS
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        queue = deque([])
        visited = set()
        queue.append(0)  # append index

        while queue:
            start = queue.popleft()
            if start in visited:
                continue
            # start + 1 and len(s) + 1, because we want to use as s[start, end]
            # end is not inclusive
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict:
                    queue.append(end)
                    if end == len(s):
                        return True
                visited.add(start)
        return False

    # DFS

    def wordBreak(self, s, wordDict):
        n = len(s)
        wordSet = set(wordDict)

        @lru_cache(None)
        def dp(start):
            if start == n:  # found a valid way to break words
                return True

            for end in range(start + 1, n + 1):  # O(n^2)
                word = s[start:end]  # O(n)
                if word in wordSet and dp(end):
                    return True
            return False
        return dp(0)

    # Word break ii

    def wordBreak2(self, s, wordDict):
        self.res = []
        self.wordDict = set(wordDict)
        self.dp = self.wordBreakDP2(s, self.wordDict)
        self.dfs(s, 0, [])
        return self.res

    def dfs(self, s, idx, path):
        if self.dp[idx + len(s)]:
            if not s:
                self.res.append(' '.join(path))
            else:
                for i in range(1, len(s) + 1):
                    if s[:i] in self.wordDict:
                        self.dfs(s[i:], idx + i, path + [s[:i]])

    def wordBreakDP2(self, s, wordDict):
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True

        for end in range(n):
            for start in range(end):
                if dp[start] and s[start:end] in wordDict:
                    dp[end] = True
        return dp

    # regular memo
    def wordBreak2RegularMemo(self, s, wordDict):
        return self.helper(s, set(wordDict), {})

    def helper(self, s: str, wordDict: set(), memo):
        if not s:
            return []
        if s in memo:
            return memo[s]
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfRest:
                    item = word + ' ' + item  # append current word to all previous word
                    res.append(item)
        memo[s] = res
        return res

    # Concatenated Words
    #
    # reverse of word break 1
    # 1. Sort the words according to shortest length since short ones form long words
    # 2. for each word start building our dictionary of words and check if word split is possible or not

    def findAllConcatenatedWordsInADict(self, words):
        res = []
        preWords = set()

        words.sort(key=len)

        for word in words:
            if self.wordBreakDP(word, preWords):
                res.append(word)
            preWords.add(word)
        return res

    # DFS solutions

    # O (N * L ^ 3), where N is number of words, L is max length of words
    def findAllConcatenatedWordsInADict(self, words):
        hashset = set(words)
        memo = {}
        res = []
        for word in words:
            if self.dfs2(word, hashset, memo):
                res.append(word)
        return res

    def dfs2(self, word, hashset, memo):
        if word in memo:
            return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            if prefix in hashset and suffix in hashset:
                memo[word] = True
                return True
            if prefix in hashset and self.dfs2(suffix, hashset):
                memo[word] = True
                return True
        memo[word] = False
        return False
