"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
"""


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1

        res = (-1, -1)
        for i in range(len(nums)-1):
            min_num = -1
            for j in range(i+1, len(nums)):
                if min_num == -1 and nums[i] < nums[j]:
                    min_num = nums[j]
                    res = (i, j)
                if nums[i] < nums[j] < min_num:
                    min_num = nums[j]
                    res = (i, j)

        if res != (-1, -1):
            nums[res[0]], nums[res[1]] = nums[res[1]], nums[res[0]]
            nums[res[0]+1:] = sorted(nums[res[0]+1:])
        else:
            nums.sort()


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1]
    s.nextPermutation(nums)
    print(nums)