# Created by matthewkight at 5/22/22
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        startColor = image[sr][sc]
        visted = set()
        stack = []

        stack.append((sr, sc))

        while len(stack):
            x, y = stack.pop()
            if not (0 <= x < len(image) and 0 <= y < len(image[0])):
                continue
            if (x, y) in visted:
                continue
            visted.add((x, y))

            if image[x][y] == startColor:
                image[x][y] = newColor

                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))
        return image






if __name__ == '__main__':
    sol = Solution()
    print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))

