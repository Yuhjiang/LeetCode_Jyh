from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums_set = set(nums)
        visited = set()

        res = []

        def dfs(pos, output):
            if pos == length:
                res.append(output)
                return
            not_visited = nums_set.difference(visited)
            for i in not_visited:
                new_output = output.copy()
                new_output.append(i)
                visited.add(i)
                dfs(pos+1, new_output)
                visited.remove(i)
        dfs(0, [])
        return res


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
