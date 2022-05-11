# Created by matthewkight at 5/10/22
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Attempt 1 - fail
        # ret_list = []
        # # used to see if we have already added the new interval
        # added = False
        # # used to see if we are in the middle of calculating the new interval
        # calculating = False
        # # what is the low end of the new interval
        # low = None
        # # what is the high end of the new interval
        # high = None
        # for interval in intervals:
        #     if interval[0] < newInterval[0] and interval[1] > newInterval[1]:
        #         # our new interval is entirly contained in the prev, can just return orig
        #         return intervals
        #
        #     if added:
        #         # If we have already added the new one we dont need to do any more
        #         ret_list.append(interval)
        #     elif interval[1] < newInterval[0]:
        #         # This interval is smaller than our new one so we can add it
        #         ret_list.append(interval)
        #     elif (interval[0] < newInterval[0] and interval[1] < newInterval[1]) or \
        #             (interval[0] > newInterval[0] and interval[1] > newInterval[1]):
        #         # we have an overlap
        #         calculating = True
        #         low = min(interval[0], newInterval[0])
        #         high = max(interval[1], newInterval[1])
        #     elif calculating:
        #         if high < interval[0]:
        #             ret_list.append([low, high])
        #             ret_list.append(interval)
        #             added = True
        #             calculating = False
        #         elif high <= interval[1]:
        #             ret_list.append([low, interval[1]])
        #             added = True
        #             calculating = False
        #     elif newInterval[0] < interval[0] and interval[1] > newInterval[0]:
        #         calculating = True
        #         low = newInterval[0]
        #         high = interval[1]
        #
        #
        # if calculating:
        #     ret_list.append([low, high])
        #     added = True
        # if not added:
        #     ret_list.append(newInterval)
        #
        #
        #
        # return ret_list

        # Attempt 2
        holder = []

        # sort into new list, not caring about overlapping, sort by first element only
        added = False
        for interval in intervals:
            if interval[0] > newInterval[0]:
                holder.append(newInterval)
                added = True

            holder.append(interval)
        if not added:
            holder.append(newInterval)

        # Now collapse the interval
        sol = [holder[0]]
        for intv in holder:
            if not (intv[0] <= sol[-1][1] and intv[1] <= sol[-1][1]):
                if intv[0] <= sol[-1][1] and intv[1] > sol[-1][1]:
                    sol[-1][1] = intv[1]
                else:
                    sol.append(intv)

        return sol







if __name__ == '__main__':
    sol = Solution()
    print(sol.insert([[1, 5]], [0, 0]))

    ary = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    print(sol.insert(ary, [4, 8]))

    ary = [[1, 5]]
    print(sol.insert(ary, [2, 3]))

    ary = [[1,3],[6,9]]
    print(sol.insert(ary, [2, 5]))
