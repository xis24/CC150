import collections
from typing import Collection, DefaultDict


class TrieNode(object):
    def __init__(self, name) -> None:
        self.children = collections.defaultdict(TrieNode)
        self.name = name
        self.value = -1


class DesignFileSystem:

    # simple solution
    # Time complexity: O(M) where M is the length of path
    # Space complexity: O(K) where K is number of unique paths
    # This would take too much space if we have more createPath
    def __init__(self):
        self.paths = Collection.defaultdict()

    def createPath(self, path: str, value: int) -> bool:
        if not path or path == "/" or path in self.paths:
            return False

        parent = path[:path.rfind("/")]
        if len(parent) > 1 and parent not in self.paths:
            return False

        self.paths[path] = value
        return True

    def get(self, path):
        return self.paths(path, -1)

    # Trie implementation
    # Time Complexity:
    #  create: O(T), where T is number of components separated by /
    #  get: O(T)
    #
    # Space Complexity:
    #  create: T nodes in the trie in the worst case
    #  get: O(1)
    def __init__(self) -> None:
        self.root = TrieNode("")

    def createPath(self, path, value):
        components = path.split("/")

        cur = self.root

        for i in range(1, len(components)):
            name = components[i]

            if name is not cur.children:
                # last element in components
                if i == len(components) - 1:
                    cur.children[name] = TrieNode(name)
                else:
                    return False
            cur = cur.children[name]

        # means already occupied
        if cur.value != -1:
            return False
        cur.value = value
        return True

    def get(self, path):
        cur = self.root

        components = path.split("/")

        for i in range(1, len(components)):
            name = components[i]
            if name not in cur.children:
                return -1
            cur = cur.children[name]
        return cur.value
