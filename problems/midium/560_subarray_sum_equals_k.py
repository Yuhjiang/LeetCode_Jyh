from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = {0: 1}
        pre = 0
        count = 0
        for i in nums:
            pre += i
            if pre - k in memo:
                count += memo[pre-k]
            if pre in memo:
                memo[pre] += 1
            else:
                memo[pre] = 1
        return count


if __name__ == '__main__':
    print(Solution().subarraySum([1,1,1], 2))
    print(Solution().subarraySum([1, 0, 1], 1))
    print(Solution().subarraySum([1], 0))
    print(Solution().subarraySum([-1, -1, 1], 0))