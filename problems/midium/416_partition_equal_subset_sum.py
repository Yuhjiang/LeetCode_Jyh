"""
https://www.kancloud.cn/kancloud/pack/70125
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False

        total_sum = sum(nums)
        if not total_sum % 2 == 0:
            return False

        target = total_sum // 2
        dp = []
        for i in range(len(nums)):
            dp.append([False for _ in range(target+1)])

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(1, target+1):
                dp[i][j] = nums[i] == j or dp[i-1][j]
                if nums[i] <= j:
                    dp[i][j] = dp[i][j] or dp[i][j-nums[i]]

        return dp[len(nums)-1][target]


class NewSolution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False

        total_sum = sum(nums)
        if not total_sum % 2 == 0:
            return False

        target = total_sum // 2
        dp = [False] * (target+1)
        dp[0] = True
        if nums[0] <= target:
            dp[nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(target, nums[i]-1, -1):
                if dp[target]:
                    return True
                dp[j] = dp[j] or dp[j-nums[i]]

        return dp[target]


if __name__ == '__main__':
    print(NewSolution().canPartition([3,3,3,4,5]))