# Created by matthewkight at 7/29/23
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        visited = set()
        rows, cols = len(grid), len(grid[0])
        max_time_to_rot = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        def infect_oranges(row, col):
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            stack = [(row, col, 0)]
            while len(stack) > 0:
                row, col, dist = stack.pop()
                visited.add((row, col))
                for x_change, y_change in dir:
                    if 0 <= row + x_change < rows and  0 <= col + y_change < cols and grid[row + x_change][col + y_change] == 1 and (row + x_change, col + y_change) not in visited:
                        visited.add((row + x_change, col + y_change))
                        max_time_to_rot[row + x_change][col + y_change] = dist + 1
                        stack.append((row + x_change, col + y_change, dist + 1))

        for i in range(rows):
            for j in range(cols):
                # 0 Empty
                # 1 Fresh
                # 2 Rotten
                if (i, j) not in visited:
                    if grid[i][j] == 0:
                        max_time_to_rot[i][j] = 0
                    if grid[i][j] == 2:
                        max_time_to_rot[i][j] = 0
                        infect_oranges(i, j)

        max_time = 0
        for row in max_time_to_rot:
            max_time = max(max(row), max_time)
        return max_time if max_time != float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(s.orangesRotting(grid))
