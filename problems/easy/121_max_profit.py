from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0

        for i, price in enumerate(prices):
            if price < min_price:
                min_price = price
            profit = price - min_price

            max_profit = profit if profit > max_profit else max_profit

        return max_profit


class NewSolution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [0] * length   # 报错每个点前最低的买入价
        max_profit = 0

        dp[0] = prices[0]
        for i in range(1, length):
            dp[i] = dp[i-1] if dp[i-1] < prices[i] else prices[i]
            max_profit = prices[i] - dp[i] if prices[i] - dp[i] > max_profit else max_profit

        return max_profit


if __name__ == '__main__':
    s = NewSolution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
