from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            tmp = target - num
            if tmp in memo:
                return [i, memo[tmp]]
            else:
                memo[num] = i


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
