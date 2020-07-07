from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                left = middle
                return left
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return left


if __name__ == '__main__':
    print(Solution().searchInsert([1,3,5,6], 5))
    print(Solution().searchInsert([1, 1, 3,5,6], 2))
    print(Solution().searchInsert([1,3,5,6], 0))
    print(Solution().searchInsert([1,3,5,6], 7))