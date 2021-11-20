from typing import Optional


class TreeNode:
    def __init__(self) -> None:
        pass


class ListNode:
    def __init__(self) -> None:
        pass


class SortedListToBST:

    # using the fact of inorder traversal
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        bst_length = self.findLength(head)
        self.head = head
        return self.convert(0, bst_length - 1)

    def findLength(self, head):
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def convert(self, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        left = self.convert(start, mid - 1)
        root = TreeNode(self.head.val)
        root.left = left
        self.head = self.head.next
        root.right = self.convert(mid + 1, end)
        return root

    # 1. find the mid node, and disconnect it from the left
    # 2. recursive on the left
    # 3. recursive on the right
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        mid = self.findMid(head)

        node = TreeNode(mid.val)

        # base case when there is just one element in the linked list
        if head == mid:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node

    def findMid(self, head):
        prev = None  # used to disconnect left half from mid
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # handling the case when slow was equal to head
        if prev:
            prev.next = None

        return slow
