from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [False] * length
        dp[0] = True

        max_dis = 0
        for i in range(length):
            if i <= max_dis:
                max_dis = i + nums[i] if i + nums[i] > max_dis else max_dis
                if max_dis >= length - 1:
                    return True

        return False


if __name__ == '__main__':
    print(Solution().canJump([3,2,2,0,4]))