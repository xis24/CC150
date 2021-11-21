from sortedcontainers import SortedDict
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

    # O(k) + O(nlog k) = O(N log K)
    def top(self, K: int) -> int:
        heap = []
        for score in self.scores.values():
            heapq.heappush(heap, score)
            if len(heap) > K:
                heapq.heappop(heap)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()

    # log(n)
    def addScore(self, playerId: int, score: int) -> None:
        # The scores dictionary simply contains the mapping from the
        # playerId to their score. The sortedScores contain a BST with
        # key as the score and value as the number of players that have
        # that score.
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            preScore = self.scores[playerId]
            val = self.sortedScores.get(-preScore)
            if val == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = val - 1

            newScore = preScore + score
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore,
                                                                 0) + 1
    # O(k)

    def top(self, K: int) -> int:
        count, total = 0, 0

        for key in self.sortedScores.keys():
            times = self.sortedScores.get(key)
            for _ in range(times):
                total += key
                count += 1

                if count == K:
                    break
            if count == K:
                break

        return -total

    # log n
    def reset(self, playerId: int) -> None:
        preScore = self.scores[playerId]
        if self.sortedScores[-preScore] == 1:
            del self.sortedScores[-preScore]
        else:
            self.sortedScores[-preScore] -= 1
        del self.scores[playerId]
