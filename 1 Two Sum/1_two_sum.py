"""
基本思路：
1. 遍历数组，计算每一个数与target的差值，以num_dict[num] = i的形式保存到字典里
2. 遍历时，在字典里寻找是否有target-num的key存在，存在的话，正好num和target-num是一对
3. 一对数据不能是相同位置的
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], i]
            else:
                num_dict[num] = i
        return None


nums = [3, 3, 11, 15]
target = 6
s = Solution()
print(s.twoSum(nums, target))