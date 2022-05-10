# Created by matthewkight at 5/10/22
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n^2 solution
        # max_profit = 0
        #
        #
        # for i in range(len(prices)-1):
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] - prices[i] > max_profit:
        #             max_profit = prices[j] - prices[i]
        #
        # return max_profit

        # n soluton
        max_profit = 0;
        if len(prices):
            smallest_num = prices[0]
            for val in prices:
                smallest_num = min(val, smallest_num)
                max_profit = max(max_profit, val-smallest_num)


        return  max_profit

if __name__ == '__main__':
    pass
