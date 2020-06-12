from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp_max = [0] * len(nums)
        dp_min = [0] * len(nums)
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])

        return max(dp_max)


class LessSpace:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp_max = nums[0]
        dp_min = nums[0]
        res = dp_max
        for i in range(1, len(nums)):
            dp_max, dp_min = max(dp_max*nums[i], dp_min*nums[i], nums[i]), \
                             min(dp_max*nums[i], dp_min*nums[i], nums[i])
            if dp_max > res:
                res = dp_max
        return res


if __name__ == '__main__':
    print(LessSpace().maxProduct([-2,3,-4]))