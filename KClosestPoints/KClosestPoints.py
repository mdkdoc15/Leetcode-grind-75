# Created by matthewkight at 9/25/22

import heapq as hq
import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        center = [0, 0]
        heap = []
        # Keep heap of points closest to K, if there is a smaller one put into  heap
        for point in points:
            dist = math.sqrt( (point[0])**2 + (point[1])**2 )
            if len(heap) < k:
                hq.heappush(heap, (-dist, point))
            elif dist < -heap[0][0]:
                hq.heappushpop(heap, (-dist, point))

        ret_list = [None] * len(heap)
        for i, val in enumerate(heap):
            ret_list[i] = val[1]

        return  ret_list

if __name__ == '__main__':
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    sol = Solution()
    print(sol.kClosest(points, k))
