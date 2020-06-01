from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)

    def binary_search(self, nums, left, right, target):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                return self.binary_search(nums, left, mid-1, target)
            else:
                return self.binary_search(nums, mid+1, right, target)
        else:
            if nums[right] >= target > nums[mid]:
                return self.binary_search(nums, mid+1, right, target)
            else:
                return self.binary_search(nums, left, mid-1, target)


if __name__ == '__main__':
    print(Solution().search([2, 1], 1))