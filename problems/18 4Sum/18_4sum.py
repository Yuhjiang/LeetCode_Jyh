"""
数组里寻找四个数字和为target
前两个定下，后两个在剩余范围内逼近
"""


class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s > target:
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return res


if __name__ == '__main__':
    nums = [-1,-5,-5,-3,2,5,0,4]
    target = -7
    s = Solution()
    print(s.fourSum(nums, target))