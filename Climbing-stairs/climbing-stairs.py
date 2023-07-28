# Created by matthewkight at 7/25/23

class Solution:
    def climbStairs(self, n: int) -> int:
        # Use de, either climbed from 1 step ago or from 2 steps ago
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(n+1):
            if i - 1 > 0 and i -2 > 0:
                dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
if __name__ == '__main__':
    s = Solution()
    x = 4
    print(s.climbStairs(x))
