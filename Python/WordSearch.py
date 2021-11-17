from typing import List
import collections

# word search i


class WordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if self.backtrack(board, i, j, word):
                    return True
        return False

    def backtrack(self, board, i, j, suffix):
        if len(suffix) == 0:  # found the word
            return True

        if i < 0 or i == self.rows or j < 0 or j == self.cols or board[i][j] != suffix[0]:
            return False

        # mark the starting position
        board[i][j] = '#'
        ret = False
        for offsetRow, offsetCol in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            ret = self.backtrack(board, i + offsetRow,
                                 j + offsetCol, suffix[1:])
            if ret:  # found the word, break to do the cleanup
                break
        board[i][j] = suffix[0]
        return ret


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    # this is not used
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


'''
Given a list words and matrix, find out all words that are in the matrix
'''


class WordSearch2:
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root  # starting node
        for w in words:
            trie.insert(w)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isword = False
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
            return
        tmp = board[i][j]  # save it so we can recover it later
        node = node.children.get(tmp)  # use trie to do the search
        if not node:  # not found
            return
        board[i][j] = "#"  # mark the starting point
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        board[i][j] = tmp
