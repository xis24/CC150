# LC 547
from collections import deque


class DisjointSet:

    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.rank = [0] * n  # union by rank

    def __len__(self):
        return self.count

    # without path compression, find is O(n), since you need to iterate through to find parent
    # with it, it's amortized O(1)
    def find(self, p):
        while p != self.parent[p]:
            # path compression
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i != j:
            if self.rank[i] < self.rank[j]:
                i, j = j, i
            self.parent[j] = i
            if self.rank[i] == self.rank[j]:
                self.rank[i] += 1
            self.count -= 1


class NumberOfProvinces:

    # DFS
    # Time complexity O(n^2)
    def findCircleNum(self, M):
        visited = [0] * len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                self.dfs(M, visited, i)
                count += 1

        return count

    def dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, visited, j)

    # BFS
    def findCircleNum2(self, M):
        visited = [0] * len(M)
        count = 0
        queue = deque([])
        for i in range(len(M)):
            if visited[i] == 0:
                queue.append(i)
                while queue:
                    front = queue.popleft()
                    visited[front] = 1
                    for j in range(len(M)):
                        if M[i][j] == 1 and visited[j] == 0:
                            queue.append(j)

                count += 1
        return count

    # union find
    def findCircleNum3(self, M):
        n = len(M)
        ds = DisjointSet(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    ds.union(i, j)
        return len(ds)
