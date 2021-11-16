import collections
from typing import OrderedDict


class Node:
    def __init___(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count


class LFUCache:

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.key_to_node = {}
        # since each count could have multiple nodes, then 2nd level is by key to node
        self.count_to_node = collections.defaultdict(OrderedDict)
        self.minCount = None

    def get(self, key):
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        # remove from count map
        del self.count_to_node[node.count][key]
        # clean memory
        if not self.count_to_node[node.count]:
            del self.count_to_node[node.count]

        node.count += 1
        self.count_to_node[node][key] = node

        # update the min count if necessary
        if not self.count_to_node[self.minCount]:
            self.minCount += 1
        return node.val

    def put(self, key, value):
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            self.get(key)  # increment count etc
            return
        if len(self.key_to_node) > self.capacity:
            k, _ = self.count_to_node[self.minCount].popitem(
                last=False)  # poped last used
            del self.key_to_node[k]
        # add new node
        self.count_to_node[1][key] = self.key_to_node[key] = Node(
            key, value, 1)
        self.minCount = 1
        return
