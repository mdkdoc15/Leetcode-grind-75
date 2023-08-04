# Created by matthewkight at 8/4/23
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Do binary search on nums bc it is in order
        i = 0
        j = len(nums) - 1
        mid = (i + j ) // 2
        if nums[mid] > target:
            # Go left
            pass
        elif nums[mid] < target:
            # Go right
            pass
        else:
            # We found number so return it's rotated index
            pass
if __name__ == '__main__':
    pass
