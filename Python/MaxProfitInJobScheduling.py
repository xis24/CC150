from typing import List
import collections


class MaxProfitInJobScheduling:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)

        # for easy comparison
        jobs = sorted(zip(startTime, endTime, profit))

        # sorted startTime to use binary search more easily
        startTime = [job[0] for job in jobs]

        self.memo = collections.defaultdict(int)
        return self.findMaxProfit(startTime, jobs, n, 0)

    def findMaxProfit(self, startTime, jobs, n, position):
        # we reached to the end
        if position == n:
            return 0

        if self.memo[position]:
            return self.memo[position]

        nextJobIndex = self.findNextJob(startTime, jobs[position][1])

        maxProfit = max(self.findMaxProfit(startTime, jobs, n, position + 1),
                        jobs[position][2] + self.findMaxProfit(startTime, jobs, n, nextJobIndex))

        self.memo[position] = maxProfit
        return maxProfit

    def findNextJob(self, startTime, lastEndPosition):
        start = 0
        end = len(startTime) - 1
        nextIndex = len(startTime)  # this value is pretty important

        while start <= end:
            mid = (start + mid) // 2
            if startTime[mid] >= lastEndPosition:
                nextIndex = mid
                end = mid - 1
            else:
                start = mid + 1

        return nextIndex

    # without stack space overhead
    # going backwards
    def findMaxProfitIterative(self, jobs, startTime, n):
        for position in range(n, -1, -1):
            currentProfit = 0
            nextIndex = self.findNextJob(startTime, self.memo[position][1])

            # this means there is a job possible, and add it's profit
            if nextIndex != n:
                currentProfit = jobs[position][2] + self.memo[nextIndex]
            else:  # only consider the current job profit
                currentProfit = jobs[position][2]

            # storing max profit we can achieve by scheduling non-conflicting jobs
            # from index position to the end of array
            if position == n - 1:  # at the beginning, no more jobs to take
                self.memo[position] = currentProfit
            else:
                self.memo[position] = max(
                    currentProfit, self.memo[position + 1])
        return self.memo[0]
