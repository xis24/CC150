class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class DesignAddAndSearch:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, 0, word)

    def dfs(self, node: TrieNode, i: int, word: str):
        if i == len(word):
            return node.isWord

        if word[i] == '.':
            for n in node.children:
                if self.dfs(node.children[n], i + 1, word):
                    return True
        if word[i] in node.children:
            return self.dfs(node.children[word[i]], i + 1, word)
        return False
