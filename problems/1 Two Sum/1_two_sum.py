"""
基本思路：
1. 遍历数组，计算每一个数与target的差值，以num_dict[num] = i的形式保存到字典里
2. 遍历时，在字典里寻找是否有target-num的key存在，存在的话，正好num和target-num是一对
3. 一对数据不能是相同位置的
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target-num], i]
            else:
                num_dict[num] = i
        return []


if __name__ == '__main__':
    s = Solution()
    import pprint
    pprint.pprint(s.twoSum([2, 7, 11, 15], 9))
    pprint.pprint(s.twoSum([4, 5, 11, 15], 8))