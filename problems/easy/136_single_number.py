"""
常规想法是用hash，但是这样子不满足题目里说的不增加额外的空间，
这里需要用一个很trick的方法，异或，可以把所有相同的值变为0，保留单个的值
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = nums[0]
        for n in nums[1:]:
            num = num ^ n

        return num


class HashSolution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = {}
        for n in nums:
            if n in nums_dict:
                del nums_dict[n]
            else:
                nums_dict[n] = 1

        return list(nums_dict.keys())[0]


class NewSolution:
    def singleNumber(self, nums: List[int]) -> int:
        num = nums[0]
        for i in nums[1:]:
            num = num ^ i

        return num


if __name__ == '__main__':
    s = NewSolution()
    print(s.singleNumber([2,2,1]))
    print(s.singleNumber([4,1,2,1,2]))