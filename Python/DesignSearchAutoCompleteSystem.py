from typing import List

# Design a search autocomplete system for a search engine. Users may input a sentence
# (at least one word and end with a special character '#').

# The hot degree for a sentence is defined as the number of times a user typed the exactly
# same sentence before.
#
# The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one).
# If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).

# If less than 3 hot sentences exist, return as many as you can.

# When the input is a special character, it means the sentence ends, and in this case, you need to
# return an empty list.


class TrieNode():
    def __init__(self) -> None:
        self.isEnd = False
        self.children = {}
        self.hot = 0


class AutocompleteSystem(object):
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.searchTerm = ""

        # 1. add historical data
        for i, sentence in enumerate(sentences):
            self.add(sentence, times[i])

    def add(self, sententce, hot):
        node = self.root
        # 2. for each character in sentence
        for c in sententce:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        # 3. when last character is added,
        #   make node.isEnd = True indicate that the current node is end of the sentence
        node.isEnd = True
        # 4. do -= because by negating, we can sort as ascending order later
        node.hot -= hot

    def search(self):
        node = self.root
        res = []
        path = ""

        for c in self.searchTerm:
            if c not in node.children:
                return res
            # 6. add each character to path variable, path will added to res when we found node.isEnd ==True
            path += c
            node = node.children[c]
        # 7. at this point, node is at the given searchTerm.
        # for ex. if search term is "i_a", we are at "a" node.
        # from this point, we need to search all the possible sentence by using DFS
        self.dfs(node, path, res)

        # 11. variable res has result of all the relevant sentences
        # we just need to do sort and return [1] element of first 3
        return [item[1] for item in sorted(res)[:3]]

    def dfs(self, node, path, res):
        # 8. check if node is end of the sentence
        # if so, add path to res
        if node.isEnd:
            # 9. when add to res, we also want to add hot for sorting
            res.append((node.hot, path))
        for c in node.children:
            self.dfs(node.children[c], path + c, res)

    def input(self, c: str) -> List[str]:
        if c != "#":
            # 5. if input is not # add c to self.searchTerm and do self.search each time
            self.searchTerm += c
            return self.search()
        else:
            self.add(self.searchTerm, 1)
            self.searchTerm = ""
