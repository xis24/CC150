class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


class MyHashMap:

    def __init__(self) -> None:
        self.size = 1000
        self.hash = [None] * self.size

    def put(self, key, value):
        index = key % self.size
        if not self.hash[index]:
            self.hash[index] = ListNode(key, value)
        else:
            curNode = self.hash[index]
            while True:
                if curNode.pair[0] == key:
                    curNode.pair = (key, value)  # update existing key,value
                    return
                if not curNode.next:
                    break
                curNode = curNode.next
            curNode.next = ListNode(key, value)

    def get(self, key):
        index = key % self.size
        curNode = self.hash[index]
        while curNode:
            if curNode.pair[0] == key:
                return curNode.pair[1]
            curNode = curNode.next
        return - 1

    def remove(self, key):
        index = key % self.size
        curNode = prev = self.hash[index]
        if not curNode:
            return
        if curNode.pair[0] == key:
            self.hash[index] = curNode.next
        else:
            curNode = curNode.next
            while curNode:
                if curNode.pair[0] == key:
                    prev.next = curNode.next
                    break
                else:
                    curNode, prev = curNode.next, prev.next
