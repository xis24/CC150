from collections import defaultdict
import heapq


class Leaderboard:
    # brute force
    # space O(n)
    def __init__(self):
        self.scores = defaultdict()

    # O(1)
    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
        else:
            self.scores[playerId] += score

    # O(nlogn)
    def top(self, K: int) -> int:
        sorted_scores = sorted(self.scores.values(), key=lambda x: -x)
        return sum(sorted_scores[:K])

    # O(1)
    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


class BetterLeaderBoard:
    # using min-heap
    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
        else:
            self.scores[playerId] += score

    #
    def top(self, K: int) -> int:
        heap = []
        for score in self.scores.values():
            heapq.heappush(heap, score)
            if len(heap) > K:
                heapq.heappop(heap)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
