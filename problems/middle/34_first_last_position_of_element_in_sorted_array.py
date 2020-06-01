from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = self.binary_search(nums, target, 0, len(nums)-1)
        if pos == -1:
            return [-1, -1]

        left, right = pos, pos
        while left >= 0 and nums[left] == target:
            left -= 1
        while right < len(nums) and nums[right] == target:
            right += 1

        return [left+1, right-1]

    def binary_search(self, nums: List[int], target: int, left: int, right: int):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            return self.binary_search(nums, target, left, mid-1)
        else:
            return self.binary_search(nums, target, mid+1, right)


class NewSolution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, True)
        if not nums or nums[left] != target:
            return [-1, -1]
        right = self.binary_search(nums, target, False)
        if nums[right] != target:
            right -= 1

        return [left, right]

    def binary_search(self, nums, target, ll):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (ll and nums[mid] == target):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    print(NewSolution().searchRange([5,7,7,8,8, 8], 8))