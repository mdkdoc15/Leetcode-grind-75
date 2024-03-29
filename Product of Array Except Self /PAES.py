# Created by matthewkight at 7/29/23
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1 , -1):
            right[i] = right[i+1] * nums[i+1]
        return [left[i] * right[i] for i in range(len(nums))]

if __name__ == '__main__':
    s = Solution()
    x = [1,2,3,4]
    print(s.productExceptSelf(x))
