from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        length = len(candidates)
        candidates.sort()

        path = []
        res = []

        def dfs(tar, begin):
            if tar == 0:
                res.append(path[:])
                return
            for i in range(begin, length):
                residue = tar - candidates[i]
                if residue < 0:
                    break
                path.append(candidates[i])
                dfs(residue, i)
                path.pop()

        dfs(target, 0)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum([3,4,5], 8))