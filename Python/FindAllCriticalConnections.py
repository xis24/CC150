from typing import List
import collections


class FindAllCriticalConnections:
    # Depth First Search for Cycle Detection
    # How does this fit in? This problem is not simply about finding a cycle
    # in an undirected graph. DFS can be easily used to detect the presence of
    # a cycle in the graph. Given that this is an undirected graph,
    # we can simply achieve that by keeping a visited dictionary/array of nodes
    # and simply check for already visited nodes during the depth-first traversal.
    #  If we find a node that is already visited, that implies the presence of a cycle.
    #  The algorithm is a bit more involved for directed graphs though due to the presence
    # of different kinds of edges.

    # Since this is a graph with no designated concept of a root node like in the case
    # of trees, we can consider any node to be the root node of our graph. Essentially,
    #  we need some node to start the traversal from, and that node becomes the root node
    # for all intents and purposes in our algorithm.

    # So how does this rank help us in detecting cycles in the graph? Well, it works exactly
    # like keeping a set of visited nodes would work. At each step of our traversal,
    # we maintain the rank of the nodes we've come across until now on the current path.
    # If at any point, we come across a neighbor that has a rank lower than the current
    # node's rank, we know that the neighbor must have already been visited. In other words,
    # if we started along a path with rank 0 from the root node and are currently at a node
    # with rank m and now we discover a node that already has a rank assigned to it and that
    #  value is 0 <= n < m, then it implies the presence of a cycle.

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.rank = {}
        self.graph = collections.defaultdict(list)
        self.conn_dict = {}

        self.formGraph(n, connections)
        self.dfs(0, 0)

        result = []
        for u, v in self.conn_dict:
            result.append([u, v])

        return result

    def dfs(self, node, discovery_rank):
        # this means this node is already visited, we just return the rank
        if self.rank[node]:
            return self.rank[node]

        # update the rank of this node
        self.rank[node] = discovery_rank

        # this is the max we have seen till now. So we start with this instead
        # of INT_MAX  or something
        min_rank = discovery_rank + 1

        for neighbor in self.graph[node]:

            # skip the parent
            if self.rank[neighbor] and self.rank[neighbor] == discovery_rank - 1:
                continue

            # recurse on the neighbor
            recursive_rank = self.dfs(neighbor, discovery_rank + 1)

            # Step 1, check if this edge needs to be discarded
            if recursive_rank <= discovery_rank:
                del self.conn_dict[min(node, neighbor), max(node, neighbor)]

            # step 2, update the min rank if needed
            min_rank = min(min_rank, recursive_rank)

        return min_rank

    def formGraph(self, n, connections):

        # default rank for unisited node is null
        self.rank = [None] * n

        for u, v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)

            self.conn_dict[min(u, v), max(u, v)] = 1
