from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # n^2 solution
    # for i in range(len(nums) - 1):
    #     for j in range(i, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    # O(n) solution
    map = {}
    for val in nums:
        map[val] = val
    for i, val in enumerate(nums):
        check = target - val
        if check in map:
            index = nums.index(check)
            if index != i:
                return [i, index]

if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
