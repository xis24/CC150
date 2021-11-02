import collections
from typing import List
import heapq


class ConnectCitiesWithMinCost:

    # Find the min spanning tree
    # O(E*log(E))
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # min spanning tree
        # prims algorithm
        # greedy algo

        # initialize a tree with a single vertex

        # city1 <-> city2 may have multiple different cost connections
        # so use a list of tuples.
        graph = collections.defaultdict(list)
        for city1, city2, cost in connections:
            graph[city1].append((cost, city2))
            graph[city2].append((cost, city1))

        # arbitary starting point cost 0, saving cost at first
        # var to use heap
        queue = [(0, n)]
        visited = set()

        total = 0

        while queue and len(visited) < n:  # exit if all cities has been visited
            cost, city = heapq.heappop(queue)
            if city not in visited:
                visited.add(city)
                total += cost
                for edge_cost, next_city in graph[city]:
                    heapq.heappush(queue, (edge_cost, next_city))
        return total if len(visited) == n else -1

    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        parents = [x for x in range(n + 1)]
        ranks = [1] * (n + 1)

        def find(u):
            while u != parents[u]:
                u = parents[parents[u]]
                u = parents[u]
            return u

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            # same parent
            if root_u == root_v:
                return False

            if ranks[root_v] > ranks[root_u]:
                root_u, root_v = root_v, root_u  # swap
            parents[root_v] = root_u  # make large ranks to have same root
            ranks[root_u] += ranks[root_v]  # move tree to large tree
            return True

        connections.sort(key=lambda x: x[2])
        ans = 0
        for u, v, cost in connections:
            if union(u, v):
                ans += cost
        root = find(n)
        return ans if all(root == find(city) for city in range(1, N + 1)) else -1
