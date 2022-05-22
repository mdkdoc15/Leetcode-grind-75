# Created by matthewkight at 5/22/22

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = 0
        max_index = len(nums) - 1
        while min_index <= max_index:
            mid_index = (min_index + max_index) // 2
            if nums[mid_index] > target:
                max_index = mid_index - 1
            elif nums[mid_index] < target:
                min_index = mid_index + 1
            else:
                return mid_index
        return -1

if __name__ == '__main__':
    pass
