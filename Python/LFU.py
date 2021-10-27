from collections import defaultdict
from typing import OrderedDict


class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count  # freq of this node


# least frequent used cache

class LFUCache:
    def __init__(self, capacity) -> None:
        self.cap = capacity
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.minCount = None

    def get(self, key):
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        # remove old freq
        del self.count2node[node.count][key]

        # clean up memory/ref
        if not self.count2node[node.count]:
            del self.count2node[node.count]

        # put latest info there
        node.count += 1
        self.count2node[node.count][key] = node

        # check mincount
        if not self.count2node[self.minCount]:
            self.minCount += 1

        return node.val

    def put(self, key, value):
        if not self.cap:
            return

        if key in self.key2node:
            self.key2node[key].val = value
            # increament the count
            self.get(key)
            return

        # capacity is full
        if len(self.key2node) == self.cap:
            k, n = self.count2node[self.minCount].popitem(last=False)
            del self.key2node[k]

        # key doesn't exist before
        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return
