import collections
from typing import List


class Node:
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.content = ""


class DesignInMemoryFileSystem:

    def __init__(self):
        self.root = Node()

    # find and return node at path
    def find(self, path, create=True):
        curr = self.root
        if len(path) == 1:
            return self.root
        for word in path.split("/")[1:]:
            if not curr.children.get(word) and not create:
                return None
            curr = curr.child[word]
        return curr

    def ls(self, path: str) -> List[str]:
        curr = self.find(path)

        if curr.content:
            return [path.split("/")[-1]]

        return sorted(curr.child.keys())

    def mkdir(self, path: str) -> None:
        self.find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.find(filePath)
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.find(filePath)
        return curr.content
