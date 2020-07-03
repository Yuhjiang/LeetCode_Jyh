from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        ans = None

        nums.sort()

        for i in range(length-2):
            left, right = i + 1, length - 1

            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if ans is None:
                    ans = tmp
                else:
                    ans = tmp if abs(tmp-target) < abs(ans-target) else ans
                if tmp < target:
                    left += 1
                else:
                    right -= 1
                if ans == target:
                    return ans
        return ans


if __name__ == '__main__':
    print(Solution().threeSumClosest([0,2,1,-3], 1))

