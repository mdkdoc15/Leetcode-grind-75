# Created by matthewkight at 7/24/23
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        number_to_index = {}
        for i, num in enumerate(nums):
            if num in number_to_index:
                number_to_index[num].append(i)
            else:
                number_to_index[num] = [i]

        result = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) -1):
                check = -(nums[i] + nums[j])
                # num_to_index is in accending order so if the last index is bigger than j then it is valid
                if number_to_index.get(check, [0])[-1] > j:
                    data = [nums[i], nums[j], check]
                    data.sort()
                    data = tuple(data)
                    result.add(data)

        return [list(tup) for tup in result]
if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(s.threeSum(nums))
