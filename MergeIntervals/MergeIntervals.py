# Created by matthewkight at 7/31/23

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        j = 1
        out = []
        while j < len(intervals):
            if intervals[i][1] >= intervals[j][0]:
                while intervals[i][1] >= intervals[j][0]:
                    j += 1
                out.append([intervals[i][0], intervals[j-1][1]])
                i = j
                j += 1
            else:
                out.append(intervals[i])
                i += 1
                j += 1
        return out

if __name__ == '__main__':
    s = Solution()
    intv = [[1,3],[2,6],[8,10],[15,18]]
    print(s.merge(intv))
