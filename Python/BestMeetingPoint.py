from typing import List


class BestMeetingPoint:

    '''
    Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.
    The total travel distance is the sum of the distances between the houses of the friends and the meeting point.
    The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
    '''

    # 1) Brute force solution,
    # from each grid, use BFS to search the steps to reach to all buildings
    # 2) Better brute force solution
    # we don't actually need to do BFS, we can use the formula to calculate the distance once we have building position
    # but still O(m^2 * n^2)

    # median would be the point where it has shortest distance to all houses
    # O(mn log(mn))
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows, cols = self.getBuilding(grid)
        x_median, y_median = self.getMedian(rows, cols)
        distance = 0
        for x in rows:
            distance += abs(x_median - x)
        for y in cols:
            distance += abs(y_median - y)
        return distance

    def getBuilding(self, grid):
        rows = []
        cols = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        return rows, cols

    def getMedian(self, rows, cols):
        rows.sort()
        cols.sort()
        return rows[len(rows) // 2], cols[len(cols) // 2]
