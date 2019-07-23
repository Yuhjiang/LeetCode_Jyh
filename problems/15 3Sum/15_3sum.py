"""
寻找数组里和为0的三个数字的组合
由数学证明可得，至多需要
C(3，N)次比较
C(3, 6) = (6 * 5 * 4) / (3 * 2 * 1)
排好序的数组里，可省略其中一些情况
left最小值
middle次小值，right最大值
通过移动middle和right找到0值
"""


class Solution:
    def threeSum(self, nums):
        length = len(nums)
        nums.sort()
        res = []
        for i in range(0, length - 2):
            # 不出现重复的情况
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, length - 1
            while left < right:

                sum_temp = nums[i] + nums[left] + nums[right]
                if sum_temp == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif sum_temp > 0:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([0,0,0]))