from typing import Optional


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    '''
        least recently used would be at the head
        recently used/added should be at the tail
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.remove(node)  # remove from current position
        self.add(node)  # add to the tail
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node = Node(key, value)
        self.hashmap[key] = node
        self.add(node)

        if len(self.hashmap) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.hashmap[node.key]

    #     A <=> B <=> C
    #           ^
    def remove(self, node):
        prev = node.prev  # A
        next = node.next  # C
        prev.next = next
        next.prev = prev

    # add tail
    def add(self, node):
        lastNode = self.tail.prev
        lastNode.next = node
        node.prev = lastNode
        node.next = self.tail
        self.tail.prev = node


class PartitionList:
    # 1 -> 4 -> 3 -> 2 -> 5 -> 2,  x = 3
    # All nodes less than x come before nodes greater or equal to x

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        firstList = firstListHead = ListNode(0)
        secondList = secondListHead = ListNode(0)

        while head:
            if head.val < x:
                firstList.next = head
                firstList = firstList.next
            else:
                secondList.next = head
                secondList = secondList.next
            head = head.next

        # break the 2nd list
        secondList.next = None
        # connection first and second, connection should be node after dummy
        firstList.next = secondListHead.next

        return firstListHead.next
