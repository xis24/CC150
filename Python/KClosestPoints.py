from typing import List
import heapq


class KClosestPoints:
    # nlog(n)
    '''
    C++'s STL, for example, uses QuickSort most of the time but will switch to either HeapSort or InsertionSort depending on the nature of the data. 
    Java uses a variant of QuickSort with dual pivots when dealing with arrays of primitive values. 
    The implementation of both C++'s and Java's sort methods will require an average of O(logN) extra space. 
    Python uses TimSort, which is a hybrid of MergeSort and InsertionSort and requires O(N) extra space. 
    '''

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=self.squared_distsance)
        return points[:k]

    def squared_distance(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2

    # max heap and max priority heap
    # Use a max heap to store points by distance
    #  store the first K elements in the heap
    #  only add new elements that are closer than the top point in the heap while removing the top point to kepp the heap at k elements

    # Time: O(nlogk)
    # Space: O(k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap
        heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)

        for i in range(k, len(points)):
            dist = -self.squared_distance(points[i])
            if dist > heap[0][0]:
                # if this point is closer than the kth farthest, discard the farthest point and add this one
                heapq.heappushpop(heap, (dist, i))
        return [points[i] for _, i in heap]

    # quick select algorithm
    # Time: O(n)
    # Space: O(1)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quickSelect(points, 0, len(points) - 1, k)
        return points[:k]

    def quickSelect(self, points, left, right, k):
        if left < right:
            p = self.partition(points, left, right, k)
            if p == k:
                return
            elif p < k:
                self.quickSelect(points, p + 1, right, k)
            else:
                self.quickSelect(points, left, p - 1, k)

    def partition(self, points, left, right, k):
        pivot = points[right]  # could be random
        a = left

        for i in range(left, right):
            dist1 = points[i][0] ** 2 + points[i][1] ** 2
            dist2 = pivot[0] ** 2 + pivot[1] ** 2
            if dist1 <= dist2:
                points[a], points[i] = points[i], points[a]
                a += 1
        points[a], points[right] = points[right], points[a]
        return a
