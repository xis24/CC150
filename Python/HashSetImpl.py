class Node:
    def __init__(self, val, node=None):
        self.value = val
        self.next = node


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, key):
        if not self.exists(key):  # check exsistence first
            newNode = Node(key, self.head.next)
            self.head.next = newNode

    def exists(self, key):
        cur = self.head.next
        while cur:
            if cur.value == key:
                return True
            cur = cur.next
        return False

    def delete(self, key):
        prev = self.head
        cur = self.head.next

        while cur:
            if cur.value == key:
                nextNode = cur.next
                prev.next = nextNode
                return
            prev = cur
            cur = cur.next


# Time Complexity: O(N / K), where N is the number of possible values
# K is number of buckets
# Space Complexity: O(K + M)

class HashSetImpl:

    def __init__(self) -> None:
        self.keyRange = 769
        self.bucket = [Bucket() for _ in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key):
        hash = self._hash(key)
        self.bucket[hash].insert(key)

    def remove(self, key):
        hash = self._hash(key)
        self.bucket[hash].delete(key)

    def contains(self, key):
        hash = self._hash(key)
        return self.bucket[hash].exists(key)
