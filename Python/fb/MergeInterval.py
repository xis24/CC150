from typing import List
import heapq


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

    '''
    Facebook followup 
    
    Question: How do you add intervals and merge them for a large stream of intervals? (Facebook Follow-up Question)
    We need to have two functions for the tree (add interval and query tree).

    '''


class TreeNode:
    def __init__(self, start, end, middle) -> None:
        self.start = start
        self.end = end
        self.middle = middle


class MergeTreeInStream:

    def __init__(self) -> None:
        self.root = None

    def merge(self, intervals: List[List[int]]):
        if not intervals:
            return []

        for start, end in intervals:
            if not self.root:
                self.root = TreeNode(start, end, (start + end) // 2)
            else:
                self.add(self.root, start, end)
        return self.query(self.root)

    def add(self, node, start, end):
        if end < node.middle:  # newly inserted node start left side of current node
            if node.left:
                self.add(node.left, start, end)
            else:
                node.left = TreeNode(start, end, (start + end) // 2)
        elif node.middle < start:  # newly inserted node start right side of current node
            if node.right:
                self.add(node.right, start, end)
            else:
                node.right = TreeNode(start, end, (start + end) // 2)
        else:
            node.start = min(node.start, start)
            node.end = max(node.end, end)

    def query(self, node):
        if not node:
            return []
        # merge sort divided conquer
        left_intervals = self.query(node.left)
        right_intervals = self.query(node.right)
        res = []

        inserted = False
        for lres in left_intervals:
            if lres[1] < node.start:
                res.append(lres)
            else:
                res.append([min(lres[0], node.start), node.end])
                inserted = True
                break
        if not inserted:
            res.append([node.start, node.end])

        for rres in right_intervals:
            if rres[0] <= node.end:
                res[-1][1] = max(node.end, rres[1])
            else:
                res.append(rres)
        return res

    # Given a list of interval already sorted by first index
    # insert an interval to the list, merge it if necessary
    # return a new list of intervals

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        ret = []
        idx, n = 0, len(intervals)

        # before the intersection of interval
        while idx < n and new_start > intervals[idx][0]:
            ret.append(intervals[idx])
            idx += 1

        # add interval if necessary
        if not ret or ret[-1][1] < new_start:
            ret.append(newInterval)
        else:
            ret[-1][1] = max(ret[-1][1], new_end)

        # add the rest
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            if ret[-1][1] < start:
                ret.append(interval)
            else:
                ret[-1][1] = max(ret[-1][1], end)
        return ret

    # meeting room ii
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = [intervals[0][1]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if rooms[0] < start:
                heapq.heappushpop(rooms, end)
            else:
                heapq.heappush(rooms, end)
        return len(rooms)

    # car pooling problem
    # [passenger, from, to]
    # return True if we can pickup and dropoff all passengers
    # O(nlogn)

    # if there is constraint on the trip values, we can use bucket sort
    # create a timestamp with that value, and do the similar thing as below
    # Time O(max(N, 1001))
    # Space O(1001) = O(1)

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[1]])
        timestamp.sort()
        used_capacity = 0
        for _, passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False
        return True
