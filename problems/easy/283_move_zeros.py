from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


if __name__ == '__main__':
    s = Solution()
    l = [0,1,0,3,12]
    s.moveZeroes(l)
    print(l)