from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        dp = {}

        def dfs(left):
            if left in dp:
                return dp[left]
            if left < 0:
                return -1
            elif left == 0:
                return 0
            min_a = amount + 1
            for i in coins:
                res = dfs(left-i)
                if 0 <= res < min_a:
                    min_a = res + 1
            dp[left] = min_a if min_a < amount+1 else -1
            return dp[left]
        res = dfs(amount)

        return res


if __name__ == '__main__':
    print(Solution().coinChange([1, 2, 5], 11))
    print(Solution().coinChange([], 1))