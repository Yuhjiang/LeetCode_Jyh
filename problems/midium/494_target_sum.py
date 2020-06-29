from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        max_sum = sum(nums)
        if max_sum < S or -max_sum > S:
            return 0

        t = max_sum * 2 + 1

        dp = []
        for i in range(len(nums)):
            dp.append([0 for _ in range(t)])

        if nums[0] == 0:
            dp[0][max_sum] = 2
        else:
            dp[0][nums[0] + max_sum] = 1
            dp[0][-nums[0] + max_sum] = 1
        for i in range(1, len(nums)):
            for j in range(0, t):
                dp[i][j] = (dp[i-1][j-nums[i]] if j - nums[i] >= 0 else 0) \
                           + (dp[i-1][j+nums[i]] if j + nums[i] < t else 0)

        return dp[len(nums)-1][S+max_sum]


if __name__ == '__main__':
    print(Solution().findTargetSumWays([1], -2))