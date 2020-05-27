"""
简单的动态规划问题
dp[i] = max(dp[i-1], dp[i-2]+nums[i]) 因为不能连续取数，所以取i-1的时候，i不能取，i-2的时候可以取
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = length * [0]

        for i in range(length):
            self.max_profit(dp, i, nums)

        return max(dp)

    def max_profit(self, dp, i, nums):
        if i-1 >= 0:
            if i-2 >= 0:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            else:
                dp[i] = max(dp[i-1], nums[i])
        else:
            dp[i] = nums[i]


class NewSolution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if not length:
            return 0
        dp = nums[:]
        for i in range(length):
            if i >= 1:
                dp[i] = dp[i-1] if dp[i-1] > dp[i] else dp[i]
            if i >= 2:
                dp[i] = dp[i-2] + nums[i] if dp[i-2] + nums[i] > dp[i] else dp[i]

        return dp[length-1] if dp[length-1] > dp[length-2] else dp[length-2]


if __name__ == '__main__':
    s = Solution()
    print(s.rob([2,7,9,3,1]))