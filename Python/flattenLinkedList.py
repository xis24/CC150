class ListNode:
    def __init__(self, val=0, next=None, down=None) -> None:
        self.val = val
        self.next = next
        self.down = down


class flattenLinkedList:

    def flatten(self, head):
        if not head:
            return head
        dummy = ListNode(next=head)
        self.dfs(head)
        return dummy.next

    def dfs(self, head):
        if not head:
            return head

        if not head.down and not head.next:
            return head

        leftTail = self.dfs(head.down)
        rightTail = self.dfs(head.next)

        if leftTail:
            leftTail.next = head.next
            head.next = head.down
            head.down = None

        return rightTail if rightTail else leftTail


if __name__ == '__main__':
    obj = flattenLinkedList()
    node = ListNode(5, ListNode(10, ListNode(19, ListNode(28, down=ListNode(35, next=ListNode(40)))), ListNode(20)),
                    ListNode(7, ListNode(8)))
    newNode = obj.flatten(node)
    while newNode:
        print(newNode.val)
        newNode = newNode.next
