"""
寻找数组里三个数字和最接近target的值
先排序，再left，right逼近
"""


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        length = len(nums)
        differ = 2 ** 32 - 1
        for i in range(0, length - 2):
            left, right = i + 1, length - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < target:
                    left += 1
                    # 判断differ是否是最小
                    if target - s < differ:
                        differ = target - s
                        res = s
                elif s > target:
                    right -= 1
                    # 判断differ是否是最小
                    if s - target < differ:
                        differ = s - target
                        res = s
                else:
                    return target
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([1, 1, 1, 0], -100))