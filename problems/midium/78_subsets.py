from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        res = []

        def dfs(pos, output):
            res.append(output)
            for i in range(pos, length):
                new_output = output.copy()
                new_output.append(nums[i])
                dfs(i+1, new_output)

        dfs(0, [])
        return res


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))