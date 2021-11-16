class Node:
    def __init__(self, val, prev, next, child):
        pass


class FlattenMultiLevelLinkedList:

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        dummy = Node(None, None, head, None)
        self.dfs(dummy, head)
        dummy.next.prev = None  # cut of the connections from the head
        return dummy.next

    '''
     1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
     child === left 
     next === right
    '''

    def dfs(self, prev, curr):
        if not curr:
            return prev
        # since these two nodes aren't connected before, connect them first
        curr.prev = prev
        prev.next = curr

        tempNext = curr.next
        tail = self.dfs(curr, curr.child)
        curr.child = None
        return self.dfs(tail, tempNext)
