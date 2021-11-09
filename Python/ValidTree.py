import collections
from typing import List


class ValidTree:

    # In order for a graph to be a valid tree, the following has to be true
    # - FULLY connected graph should have n - 1 edges

    # we need to check the following
    # 1. check whether or not there are n - 1 edges. If there is not, return false
    # 2. check whether or not the graph is fully connected. return true if it's. false otherwise

    # Iteritve DFS
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:  # first requirement
            return False

        # create adj list
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        # we will need a seen set to prevent our code from infinite looping
        seen = {0}
        stack = [0]

        while stack:
            node = stack.pop()
            for nei in adj_list[node]:
                if nei in seen:
                    continue
                seen.add(nei)
                stack.append(nei)
        return len(seen) == n

    # recursive DFS

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:  # first requirement
            return False

        # create adj list
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        seen = set()

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for nei in adj_list[node]:
                dfs(nei)

        dfs(0)  # start from 0
        return len(seen) == n

    # BFS
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:  # first requirement
            return False

        # create adj list
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        seen = {0}
        queue = collections.deque([0])

        while queue:
            node = queue.popleft()
            for nei in adj_list[node]:
                if nei in seen:
                    continue
                queue.append(nei)
                seen.add(nei)
        return len(seen) == n

    # several stratigies of detecting whether or not an undirected graph
    # contians cycles.
    # First strategy is simply delete the opposite direction edges from
    # the graph. For example, if we are A -> B, we should look B's neighbors
    # and delete A from it.

    # // While there are nodes remaining on the stack...
    # while (!stack.isEmpty()) {
    #     int node = stack.pop(); // Take one off to visit.
    #     // Check for unseen neighbours of this node:
    #     for (int neighbour : adjacencyList.get(node)) {
    #         // Check if we've already seen this node.
    #         if (seen.contains(neighbour)) {
    #             return false;
    #         }
    #         // Otherwise, put this neighbour onto stack
    #         // and record that it has been seen.
    #         stack.push(neighbour);
    #         seen.add(neighbour);
    #         // Remove the link that goes in the opposite direction.
    #         adjacencyList.get(neighbour).remove(node);
    #     }
    # }

    # Second Strategy is to use a seen map, that keeps track of the parent
    # node that we got to a node from. Then when we iterate through the
    # neighbors of a node, we ignore the parent node as otherwise, it'll
    # be detected as a trivial cycle. the starting node has no "parent",
    # so put it as -1
    # Time complexity: O(N + E)
    # Space: O(N + E)

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:  # first requirement
            return False

        # create adj list
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        parent = {0: -1}
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbor in adj_list[node]:
                if neighbor == parent[node]:
                    continue
                if neighbor in parent:  # if we already seen this node
                    return False
                parent[neighbor] = node  # document the parent
                stack.append(neighbor)
        return len(parent) == n

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:  # first requirement
            return False

        # create adj list
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        seen = set()

        def dfs(node, parent):
            seen.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if neighbor in seen:
                    return False
                result = dfs(neighbor, node)
                if not result:
                    return False
            return True

    # We return true iff no cycles were detected,
    # AND the entire graph has been reached.
        return dfs(0, -1) and len(seen) == 0

    # BFS
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:  # first requirement
            return False

        # create adj list
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        parent = {0: -1}
        queue = collections.deque([0])

        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if neighbor in parent:
                    return False
                parent[neighbor] = node
                queue.append(neighbor)
        return len(parent) == n
