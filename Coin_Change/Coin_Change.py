# Created by matthewkight at 7/28/23
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP
        if amount ==0:
            return amount
        change_amt = [float('inf')] * (amount + 1)

        for coin in coins:
            if coin <= amount:
                change_amt[coin] = 1

        for i in range(len(change_amt)):
            pos_vals = [change_amt[i-j] + 1 for j in coins if i-j >= 0]
            pos_vals.append(change_amt[i])
            change_amt[i] = min(pos_vals)

        return change_amt[amount] if change_amt[amount] != float('inf') else -1

if __name__ == '__main__':
    s = Solution()
    coins = [1]
    amount = 1
    print(s.coinChange(coins, amount))
