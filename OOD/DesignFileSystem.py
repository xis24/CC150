import collections
from typing import List


class Node:
    def __init__(self) -> None:
        self.children = collections.defaultdict(Node)
        self.content = ""


class FileSystem:

    def __init__(self) -> None:
        self.root = Node()

    def ls(self, path: str) -> List[str]:
        cur = self.find(path)
        # assume operation is valid, no need to check null;if there is content, this must be a file
        if cur.content:
            return [path.split("/")[-1]]
        return sorted(cur.children.keys())

    def find(self, path, create=True):
        cur = self.root
        if len(path) == 1:
            return self.root
        for word in path.split("/")[1:]:
            if not cur.chilren.get(word) and not create:
                return None
            cur = cur.children[word]
        return cur

    def mkdir(self, path: str) -> None:
        self.find(path)

    def addContentToFile(self, filePath: str, content):
        cur = self.find(filePath)
        if not cur:
            return None
        cur.content += content

    def readContentFromFile(self, filePath):
        cur = self.find(filePath)
        if not cur:
            return None
        return cur.content
