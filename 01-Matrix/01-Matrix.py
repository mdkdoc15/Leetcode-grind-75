# Created by matthewkight at 5/11/22
from typing import List


class Solution:
    def distance(self, tup1 : tuple, tup2 : tuple) -> int:
        return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Attempt 1 - Brute force
        # sol = []
        # # set up the matrix
        # for i, row in enumerate(mat):
        #     sol.append([])
        #     for j, col in enumerate(row):
        #         sol[i].append(float('inf'))
        #
        # # Set all the zeros
        # for i, row in enumerate(mat):
        #     for j, col in enumerate(row):
        #         if mat[i][j] == 0:
        #             sol[i][j] = 0
        #
        # # Find everything that is not zero. Look around to find it's closest
        # for i, row in enumerate(mat):
        #     for j, col in enumerate(row):
        #         if sol[i][j] != 0:
        #
        #
        # # keep searching until you have searching until you find a zero, then return distacne to that 0
        # def findClosestZero(self, i , j) -> int:
        #     queue = []
        #     # Add all of the neighbors
        #     queue.append((i + 1,j))
        #     queue.append((i - 1,j))
        #     queue.append((i,j + 1))
        #     queue.append((i,j - 1))

        # # Attempt 2 - using a dict - Works but needs to be more efficient
        #
        # sol = []
        # dic = {0: [], 1 : []}
        # for i, row in enumerate(mat):
        #     sol.append([])
        #     for j, col in enumerate(row):
        #         sol[i].append(0)
        #         if col == 0:
        #             dic[0].append((i, j))
        #         else:
        #             dic[1].append((i, j))
        #
        #
        #
        # for tup in dic[1]:
        #     min_val = float('inf')
        #     for tup2 in dic[0]:
        #         dist = self.distance(tup, tup2)
        #         min_val = min(min_val, dist)
        #     sol[tup[0]][tup[1]] = min_val
        #
        # return sol


        # Attempt 3 - DP


        sol = []
        # set up the matrix
        for i, row in enumerate(mat):
            sol.append([])
            for j, col in enumerate(row):
                sol[i].append(float('inf'))

        # set up the matrix
        for i, row in enumerate(mat):
            for j, col in enumerate(row):
                if mat[i][j] == 0:
                    sol[i][j] = 0
                else:
                    if i > 0:
                        sol[i][j] = min(sol[i][j], sol[i-1][j] + 1)
                    if j > 0:
                        sol[i][j] = min(sol[i][j], sol[i][j- 1] + 1)

        for i in reversed(range(len(mat))):
            for j in reversed(range(len(mat[i]))):

                if i < len(mat) - 1:
                    sol[i][j] = min(sol[i][j], sol[i+1][j] + 1)
                if j < len(mat[0]) - 1:
                    sol[i][j] = min(sol[i][j], sol[i][j+ 1] + 1)
        return sol





if __name__ == '__main__':
    sol = Solution()
    print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
