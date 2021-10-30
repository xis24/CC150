# LC 863
# All Nodes Distance K in binary Tree
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    # convert tree problem to a graph
    graph = collections.defaultdict(list)
    self.buildGraph(root, None, graph)

    queue = collections.deque([(target, 0)])
    visited = set()
    ans = []

    while queue:
        node, distance = queue.popleft()
        if node in visited:
            continue
        visited.add(node)

        if k == distance:
            ans.append(node)
        elif k < distance:
            for child in graph:
                queue.append((child, distance + 1))
    return ans


def buildGraph(self, node, parent, graph):
    if not node:
        return
    if parent:
        graph[node].append(parent)
    if node.left:
        graph[node].append(node.left)
        self.buildGraph(node.left, node, graph)
    if node.right:
        graph[node].append(node.right)
        self.buildGraph(node.right, node, graph)
