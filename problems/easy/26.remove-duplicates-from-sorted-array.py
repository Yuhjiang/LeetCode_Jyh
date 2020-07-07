from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pre = None
        pos = 0

        for i in range(len(nums)):
            if nums[i] != pre:
                nums[pos] = nums[i]
                pos += 1
                pre = nums[i]

        return pos


if __name__ == '__main__':
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(Solution().removeDuplicates([1, 1, 2]))
    print(Solution().removeDuplicates([1]))