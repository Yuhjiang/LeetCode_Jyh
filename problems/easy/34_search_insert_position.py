from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        index = self.binary_search(nums, target, left, right)
        return index

    def binary_search(self, nums, target, left, right):
        middle = (left + right) // 2

        if target == nums[middle]:
            return middle

        if right - left == 1:
            if nums[left] < target < nums[right]:
                return left + 1
            elif target < nums[left]:
                return left - 1 if left > 0 else 0
            elif target == nums[left]:
                return left
            elif target == nums[right]:
                return right
            else:
                return right + 1
        elif left == right:
            if target < nums[left]:
                return left - 1 if left > 0 else 0
            else:
                return left + 1

        if target < nums[middle]:
            return self.binary_search(nums, target, left, middle)
        elif target > nums[middle]:
            return self.binary_search(nums, target, middle, right)


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))
    print(s.searchInsert([1, 3, 5, 6], 2))
    print(s.searchInsert([1, 3, 5, 6], 7))
    print(s.searchInsert([1, 3, 5, 6], 0))
    print(s.searchInsert([1, 3], 3))
    print(s.searchInsert([1, 3, 5], 4))