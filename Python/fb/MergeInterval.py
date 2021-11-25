from typing import List


class MergeInterval:

    '''
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    '''

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ret = []

        for start, end in intervals:
            if not ret or ret[-1][1] < start:
                ret.append([start, end])
            else:
                ret[-1][1] = max(ret[-1][1], end)
        return ret
