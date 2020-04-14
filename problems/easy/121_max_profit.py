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


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
