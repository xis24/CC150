class RotateMatrix:
    def rotate(self, grid):
        # rows = len(matrix)
        # cols = len(matrix[0])

        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # res = [[None] * cols for _ in range(rows)]

        # level = rows // 2 if rows % 2 == 0 else rows // 2 + 1

        # for i in range(level):
        #     total = (cols - i * 2) * 2 + (rows - i * 2) * 2 - 4
        #     r, c = i, i
        #     idx = 0
        #     while total:
        #         row, col = r + directions[idx][0], c + directions[idx][1]
        #         if row < 0 or row >= rows or col < 0 or col >= cols or  \
        #                 (isinstance(matrix[row][col], int) and matrix[row][col] < i):
        #             idx += 1
        #             continue
        #         res[row][col] = matrix[r][c]
        #         matrix[r][c] = i
        #         r, c = row, col
        #         total -= 1
        rows, cols = len(grid), len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[None] * cols for _ in range(rows)]
        level = rows // 2 if rows % 2 == 0 else rows // 2 + 1
        for l in range(level):
            total = (cols - l * 2) * 2 + (rows - l * 2) * 2 - 4
            r, c = l, l
            idx = 0
            while total:
                row, col = r + directions[idx][0], c + directions[idx][1]
                if row < 0 or row >= rows or col < 0 or col >= cols or (isinstance(grid[row][col], int) and grid[row][col] < l):
                    idx += 1
                    continue
                res[row][col] = grid[r][c]
                grid[r][c] = l
                r, c = row, col
                total -= 1
        for li in res:
            print(li)


if __name__ == '__main__':
    obj = RotateMatrix()
    res = obj.rotate([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])
    # for i in range(len(res)):
    #     s = ''
    #     for j in range(len(res[0])):
    #         s += res[i][j]
    #     print(s)
