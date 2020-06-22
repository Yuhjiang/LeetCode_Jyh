"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-lab/
"""
from typing import List
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = []
        for _ in range(len(prices)):
            dp.append([0, 0])

        for i, price in enumerate(prices):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -price
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+price)
            if i == 1:
                dp[i][1] = max(dp[i-1][1], -price)
            else:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0]-price)

        return dp[len(prices)-1][0]


class NewSolution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        last_yesterday = 0
        dp_i_0 = 0
        dp_i_1 = -inf
        for i, price in enumerate(prices):
            temp = dp_i_0
            dp_i_0 = max(temp, dp_i_1+price)
            dp_i_1 = max(dp_i_1, last_yesterday-price)
            last_yesterday = temp

        return dp_i_0


if __name__ == '__main__':
    print(NewSolution().maxProfit([1,2,3,0,2]))
