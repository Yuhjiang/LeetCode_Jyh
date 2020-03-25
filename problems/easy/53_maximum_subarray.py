from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_sum = 0
        for i, num in enumerate(nums):
            temp_sum = current_sum + num
            if temp_sum > current_max:
                current_max = temp_sum
            if num < 0 and temp_sum < 0:
                current_sum = 0
            else:
                current_sum = temp_sum

        return current_max


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray([-2, -3, -1]))
