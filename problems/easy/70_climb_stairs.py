"""
这道题很直观的就是动态规划问题，i为要爬的阶数
dp[i] = dp[i-1] + 1
dp[i] = dp[i-2 + 2
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            if i - 1 >= 0:
                dp[i] += dp[i-1]
            if i - 2 >= 0:
                dp[i] += dp[i-2]
        return dp[n]


class newSolution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n+1):
            if i > 0:
                dp[i] += dp[i-1]
            if i > 1:
                dp[i] += dp[i-2]

        return dp[n]


if __name__ == '__main__':
    s = newSolution()
    print(s.climbStairs(44))
    print(s.climbStairs(2))
    print(s.climbStairs(1))