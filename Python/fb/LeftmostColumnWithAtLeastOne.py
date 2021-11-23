# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class LeftmostColumnWithAtLeastOne:

    # Brute force solution would be from left to right, top to bottom to see if we found the cell which has value == 1
    # O(n * m)

    # for each row, binary search the index of first 1
    # O ( mlog(n)), where m is rows, n is cols
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        curMin = cols
        for row in range(rows):
            # this will give us the index of first one in a row
            col = self.findFirstOne(binaryMatrix, row, cols)
            # we need to double check if this cell is 1
            if binaryMatrix.get(row, col) == 1:
                # remember to use min col
                curMin = min(curMin, col)
        return curMin if curMin != cols else -1

    def findFirstOne(self, binaryMatrix, rows, cols):
        left = 0
        right = cols - 1

        while left < right:
            mid = (left + right) // 2
            if binaryMatrix.get(rows, mid) == 0:
                left = mid + 1
            else:
                right = mid
        return left

        # we can start from the upper right corner, and work way to lower left
        # if we see a matrix(x, y) == 0, we move down
        # if we see a matrix(x, y) == 1, we move left
        # while we are moving, we record the result only when matrix(x, y) == 1
        # O(m + n)

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        curRow, curCol = 0, cols - 1
        ret = -1
        while curRow < rows and curCol >= 0:
            if binaryMatrix.get(curRow, curCol) == 0:
                curRow += 1
            else:
                ret = curCol
                curCol -= 1
        return ret
