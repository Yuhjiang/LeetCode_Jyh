from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        length = len(nums)
        left = [0] * length
        right = [0] * length
        left[0] = 1
        right[-1] = 1

        for i in range(1, length):
            left[i] = left[i-1] * nums[i-1]
        for j in range(length-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        for i in range(length):
            nums[i] = left[i] * right[i]

        return nums


class NewSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        length = len(nums)
        res = length * [0]
        res[0] = 1

        for i in range(1, length):
            res[i] = res[i-1] * nums[i-1]

        right = 1
        for j in range(length - 1, -1, -1):
            res[j] = res[j] * right
            right *= nums[j]

        return res


if __name__ == '__main__':
    print(NewSolution().productExceptSelf([1, 2, 3, 4]))