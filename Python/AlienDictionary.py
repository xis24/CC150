from typing import List
from collections import defaultdict, deque


class AlienDictionary:

    def alienOrder(self, words: List[str]) -> str:
        # initialize data structure
        # store character mapping from one c -> its children
        adj_list = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        # build the graph and fill the indegree as well
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:  # this only execute if above inner loop doesn't encounter break, and finish inner loop
                # check that second word isn't a prefix of first word
                if len(second_word) < len(first_word):
                    return ""

        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            front = queue.popleft()
            in_degree[front] -= 1
            output.append(front)

            for neigh in adj_list[front]:
                in_degree[neigh] -= 1
                if in_degree == 0:
                    queue.append(neigh)

        return "" if len(output) < len(in_degree) else "".join(output)


class VerifyingAlienDictionary:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for idx, c in enumerate(order):
            order_map[c] = idx

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j > len(words[i + 1]):
                    return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False
                    break
        return True
