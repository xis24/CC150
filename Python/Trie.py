from collections import defaultdict

# Space O(T) where T is total of Trie nodes
# in the worst case it's total number of characters
# of words we inserted


class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.isWord = False

    # Time O(word)
    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.isWord = True

    # Time O(word)
    def search(self, word) -> bool:
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

    # Time O(prefix)
    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
