# Created by matthewkight at 5/23/22
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n) sol
        max_sum = 0
        curr = 0
        for i, val in enumerate(nums):
            curr += val
            if curr < 0:
                curr = 0
            else:
                max_sum = max(max_sum, curr)
        if max_sum == 0:
            max_sum = max(nums)w
        return max_sum




if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-1]))
