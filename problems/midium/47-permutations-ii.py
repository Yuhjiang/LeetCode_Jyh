from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums_set = set(range(length))
        nums.sort()
        visited = set()

        ans = []

        def dfs(pos, output):
            if pos == length:
                ans.append(output)
                return
            not_visited = list(nums_set.difference(visited))
            for i in range(len(not_visited)):
                m = not_visited[i]
                if i > 0 and nums[not_visited[i]] == nums[not_visited[i-1]]:
                    continue
                new_output = output.copy()
                new_output.append(nums[m])
                visited.add(m)
                dfs(pos+1, new_output)
                visited.remove(m)

        dfs(0, [])
        return ans


if __name__ == '__main__':
    # print(Solution().permuteUnique([1,1,2]))
    print(Solution().permuteUnique([3, 3, 0, 3]))