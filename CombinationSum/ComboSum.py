# Created by matthewkight at 8/4/23
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        dp = [[] for _ in range(target+1)]
        candidates.sort()
        for candidate in candidates:
            if candidate <= target:
                dp[candidate].append([candidate])
            else:
                break
        for i in range(target+1):
            for candidate in candidates:
                if i - candidate >= 0:
                    for x in dp[i-candidate]:
                        dp[i].append(x[:] + [candidate])
                else:
                    break

        out = set()
        for el in dp[target]:
            out.add((tuple(sorted(el))))

        return [[el for el in tup] for tup in out]

if __name__ == '__main__':
    s = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(s.combinationSum(candidates, target))
