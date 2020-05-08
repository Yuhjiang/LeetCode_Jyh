from typing import List
"""
遍历数组，找到不符合升序的最左边和最右边位置
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = len(nums), 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    left = min(left, i)
                    right = max(right, j)
        return right - left + 1 if right - left > 0 else 0


"""
排序，排序前后位置不一致的为未排序的
"""


class SortSolution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left, right = len(nums), 0
        for i in range(len(nums)):
            if sorted_nums[i] != nums[i]:
                left = min(left, i)
                right = max(right, i)
        return right - left + 1 if right - left > 0 else 0


class StackSolution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        left, right = len(nums), 0
        for i, num in enumerate(nums):
            while stack and num < nums[stack[-1]]:
                left = min(left, stack.pop())
            stack.append(i)
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[j] > nums[stack[-1]]:
                right = max(right, stack.pop())
            stack.append(j)

        return right - left + 1 if right - left > 0 else 0


class NewSolution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = len(nums), 0
        if not nums:
            return 0
        min_num = nums[-1]
        max_num = nums[0]
        for i in range(len(nums)-1, -1, -1):
            left = i if nums[i] > min_num else left
            min_num = min(min_num, nums[i])
        for j in range(len(nums)):
            right = j if nums[j] < max_num else right
            max_num = max(max_num, nums[j])

        return right - left + 1 if right - left > 0 else 0


if __name__ == '__main__':
    print(NewSolution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))