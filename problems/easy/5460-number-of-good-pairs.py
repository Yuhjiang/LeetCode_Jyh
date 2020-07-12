from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        memo = {}
        for n in nums:
            if n in memo:
                memo[n] += 1
            else:
                memo[n] = 1

        ans = 0

        for key, value in memo.items():
            if value <= 1:
                continue
            elif value == 2:
                ans += 1
            else:
                ans += value * (value-1) // 2

        return ans


if __name__ == '__main__':
    print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
    print(Solution().numIdenticalPairs([1,2,3]))