from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        total = len(nums)
        left, right = 1, total - 1
        result = -1

        while left <= right:
            middle = (left + right) >> 1
            count = 0

            for i in nums:
                if i <= middle:
                    count += 1

            if count <= middle:
                left = middle + 1
            else:
                right = middle - 1
                result = middle

        return result


if __name__ == '__main__':
    print(Solution().findDuplicate([1, 2, 3, 2]))