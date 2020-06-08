from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        length = len(nums)
        pos = length - 1
        while pos > 0 and nums[pos-1] >= nums[pos]:
            pos -= 1

        if pos:
            next_pos = length - 1
            while next_pos >= pos and nums[next_pos] <= nums[pos-1]:
                next_pos -= 1
            nums[pos-1], nums[next_pos] = nums[next_pos], nums[pos-1]

        i, j = pos, length - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    nums = [3, 2, 1]
    s = Solution().nextPermutation(nums)
    print(nums)