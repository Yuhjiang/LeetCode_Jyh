from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[pos] = nums[i]
                pos += 1
        return pos


if __name__ == '__main__':
    print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))