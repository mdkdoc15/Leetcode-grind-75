# Created by matthewkight at 7/29/23

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Go thru every point ( That is not visted )
        # Do BFS on that point
        # Count the number of times BFS is performed


        to_visit = set()
        for i, lst in enumerate(grid):
            for j, val in enumerate(lst):
                if val == '1':
                    # If it is a land we will want to check it
                    to_visit.add((i,j))

        num_islands = 0
        while len(to_visit) != 0:
            index = None
            for i, j in to_visit:
                index = i, j
                break
            to_visit.remove(index)
            num_islands += 1
            to_visit = self.find_island(to_visit, index, grid)

        return num_islands
    def find_island(self, to_visit, index, grid):
        stack = [index]
        m, n = len(grid), len(grid[0])
        while len(stack) > 0:
            x, y = stack.pop()
            if self.valid_pos(x - 1, y, m, n) and grid[x-1][y] == '1' and (x-1, y) in to_visit:
                stack.append((x-1, y))
                to_visit.discard((x-1, y))
            if self.valid_pos(x + 1, y, m, n) and grid[x+1][y] == '1' and (x+1, y) in to_visit:
                stack.append((x+1, y))
                to_visit.discard((x+1, y))
            if self.valid_pos(x, y- 1, m, n) and grid[x][y-1] == '1' and (x, y-1) in to_visit:
                stack.append((x, y - 1))
                to_visit.discard((x, y - 1))
            if self.valid_pos(x, y + 1, m, n) and grid[x][y+1] == '1' and (x, y+1) in to_visit:
                stack.append((x, y + 1))
                to_visit.discard((x, y + 1))
        return to_visit


    def valid_pos(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n


if __name__ == '__main__':
    s = Solution()
    ary = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    print(s.numIslands(grid=ary))
