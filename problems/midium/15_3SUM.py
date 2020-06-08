from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums)-1

            while left < right:
                t = nums[i] + nums[left] + nums[right]
                if t == 0:
                    if left > i + 1 and nums[left] == nums[left - 1]:
                        left += 1
                        continue
                    if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                        right -= 1
                        continue
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif t > 0:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    print(Solution().threeSum([-2,0,1,1,2]))