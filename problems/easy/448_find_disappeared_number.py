from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for n in range(1, len(nums)+1):
            nums_dict[n] = 1
        for n in nums:
            if n in nums_dict:
                del nums_dict[n]

        return list(nums_dict.keys())


class NewSolution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            # 把当前访问的值对应的数组元素置为负数
            nums[abs(n)-1] = -(abs(nums[abs(n)-1]))

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res


if __name__ == '__main__':
    NewSolution().findDisappearedNumbers([4,3,2,7,8,2,3,1])