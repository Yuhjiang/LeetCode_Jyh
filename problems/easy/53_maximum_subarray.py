from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_sum = 0
        for i, num in enumerate(nums):
            temp_sum = current_sum + num
            if temp_sum > current_max:
                current_max = temp_sum
            if num < 0 and temp_sum < 0:
                current_sum = 0
            else:
                current_sum = temp_sum

        return current_max


class DivideSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self._max_sub_array(nums, 0, len(nums) - 1)

    def _max_sub_array(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        return max(self._max_sub_array(nums, left, mid),
                   self._max_sub_array(nums, mid+1, right),
                   self._max_mid_array(nums, left, mid, right))

    def _max_mid_array(self, nums, left, mid, right):
        left_max_sum = 0
        left_temp = 0
        for i in range(mid - 1, left - 1, -1):
            left_temp += nums[i]
            left_max_sum = max(left_max_sum, left_temp)

        right_max_sum = 0
        right_temp = 0
        for j in range(mid + 1, right + 1):
            right_temp += nums[j]
            right_max_sum = max(right_max_sum, right_temp)

        return left_max_sum + nums[mid] + right_max_sum


class newSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        last = nums[0]
        max_res = last
        for num in nums[1:]:
            last = last + num if last + num > num else num
            max_res = max_res if max_res > last else last

        return max_res


if __name__ == '__main__':
    s = newSolution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print(s.maxSubArray([-2, -3, -1]))
    print(s.maxSubArray([1, 2]))