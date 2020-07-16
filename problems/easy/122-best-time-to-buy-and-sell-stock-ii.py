from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)

        prev_0, prev_1 = 0, -prices[0]

        for i in range(1, n):
            prev_0 = max(prev_0, prev_1 + prices[i])
            prev_1 = max(prev_1, prev_0 - prices[i])

        return prev_0


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))
    print(Solution().maxProfit([1,2,3,4,5]))
    print(Solution().maxProfit([7,6,4,3,1]))
    print(Solution().maxProfit([]))