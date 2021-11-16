from typing import List, Optional
import heapq


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        pass


class MergeTwoSortedLists:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l2 or l1
        cur = dummy = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next

    # O(n log k)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if n > 0 else None

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = head = ListNode()
        queue = []
        count = 0  # break the tie

        for l in list:
            if l:
                count += 1
                heapq.heappush(queue, (l.val, count, l))

        while queue:
            _, _, cur.next = heapq.heappop(queue)
            cur = cur.next
            if cur.next:
                count += 1
                heapq.heappush(queue, (cur.next.val, count, cur.next))
        return head.next

    '''
    1 -> 2 -> 3 -> 4
    =>  1 -> 4 -> 2 -> 3
    '''

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head

        slow = self.findMid(head)

        head2 = self.reverse(slow.next)
        slow.next = None

        while head and head2:
            tmp1 = head.next
            tmp2 = head2.next
            head2.next = head.next
            head.next = head2
            head = tmp1
            head2 = tmp2

    def findMid(self, node):
        slow = fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, node):
        prev = None
        cur = node
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    # Copy list with random pointer

    def copyRandomList(self, head: 'Node') -> 'Node':
        return self.copyDfs(head, {})

    def copyDfs(self, head, visited):
        if not head:
            return head
        if head in visited:
            return visited[head]
        node = Node(head.value, None, None)
        visited[head] = node
        node.next = self.copyDfs(head.next, visited)
        node.random = self.copyDfs(node.random, visited)
        return node

    # LFU
