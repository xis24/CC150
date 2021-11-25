import collections


class ShortestDistanceFromGuard:
    '''
    Replace all of O with their shorted distance to guard
        O => Open Space
        G => Guard
        W => Wall
    '''

    def fillShortedDistance(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        queue = collections.deque([])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 'G':
                    grid[row][col] = 0
                    queue.append((row, col, 0))
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            x, y, step = queue.popleft()
            for offsetX, offsetY in DIR:
                newX = x + offsetX
                newY = y + offsetY
                if self.isValid(newX, newY, grid):
                    if grid[newX][newY] == 'W':
                        grid[newX][newY] = -1
                    elif grid[newX]:
                        updatedStep = step + 1
                        grid[newX][newY] = updatedStep
                        queue.append((newX, newY, updatedStep))

    def isValid(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])


if __name__ == '__main__':
    obj = ShortestDistanceFromGuard()
    grid = [
        ['O', 'O', 'O', 'O', 'G'],
        ['O', 'W', 'W', 'O', 'O'],
        ['O', 'O', 'O', 'W', 'O'],
        ['G', 'W', 'W', 'W', 'O'],
        ['O', 'O', 'O', 'O', 'G']
    ]
    obj.fillShortedDistance(grid)
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         print
    print(grid)
