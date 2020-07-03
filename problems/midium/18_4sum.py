from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        if length <= 3:
            return []

        ans = []
        nums.sort()
        for left in range(length-3):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            for right in range(left+1, length-2):
                if right > left + 1 and nums[right] == nums[right-1]:
                    continue
                l, r = right+1, length-1
                while l < r:
                    tmp = nums[left] + nums[right] + nums[l] + nums[r]
                    if tmp == target:
                        if l > right+1 and nums[l] == nums[l-1]:
                            l += 1
                            continue
                        if r < length-1 and nums[r] == nums[r+1]:
                            r -= 1
                            continue
                        ans.append([nums[left], nums[right], nums[l], nums[r]])
                        l += 1
                    elif tmp < target:
                        l += 1
                    else:
                        r -= 1
        return ans


if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution().fourSum([-3,-2,-1,0,0,1,2,3], 0))
    print(Solution().fourSum([-5,-5,-3,2,-1, 0,4, 5], -7))
