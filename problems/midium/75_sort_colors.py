from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_dict = {0: 0, 1: 0, 2: 0}
        for num in nums:
            count_dict[num] += 1

        pos = 0
        for key, items in count_dict.items():
            for i in range(items):
                nums[pos] = key
                pos += 1


class NewSolution:
    def sortColors(self, nums: List[int]) -> None:
        length = len(nums)
        p0, p2, curr = 0, length - 1, 0

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:
                curr += 1


if __name__ == '__main__':
    s = [2,0,2,1,1,0]
    NewSolution().sortColors(s)
    print(s)