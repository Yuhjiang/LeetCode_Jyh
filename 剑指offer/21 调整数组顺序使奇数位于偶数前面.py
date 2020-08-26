from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        l, r = 0, len(nums)-1
        while l < r:
            while l < len(nums) and nums[l] % 2 == 1:
                l += 1
            while r >= 0 and nums[r] % 2 == 0:
                r -= 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        return nums


if __name__ == '__main__':
    print(Solution().exchange([2, 1]))
    print(Solution().exchange([1, 2, 3, 4]))
    print(Solution().exchange([1]))
    print(Solution().exchange([1, 3, 5]))