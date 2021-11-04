from typing import List
from functools import lru_cache


class AllPathsFromSourceToTarget:

    # In directly acyclic graph (DAG), no cycle. Node starts from 0 to n - 1.
    # Find all paths from node 0 to node n - 1.
    # return any order

    # Time complexity: O(2 ^ N * N)
    #    there could be at most 2 ^ (N - 1) paths in the graph
    #    for each path, there could be n - 2 intermediate nodes, and O(N) to build a path
    # Space complexity:
    #
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ret = []
        start = 0
        path = [0]
        self.dfs(start, path, ret, graph)
        return ret

    def dfs(self, currentNode, path, ret, graph):
        if currentNode == len(graph) - 1:
            ret.append(list(path))
            return

        for nextNode in graph[currentNode]:
            path.append(nextNode)
            self.dfs(nextNode, path, ret, graph)
            path.pop()

    # Cached verison

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1

        # apply the memoization
        @lru_cache(maxsize=None)
        def allPathsToTarget(currNode):
            if currNode == target:
                return [[target]]

            results = []
            for nextNode in graph[currNode]:
                for path in allPathsToTarget(nextNode):
                    results.append([currNode] + path)

            return results

        return allPathsToTarget(0)
