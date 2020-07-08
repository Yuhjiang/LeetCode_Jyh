from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        ans = []
        length = len(candidates)
        candidates.sort()

        def dfs(tar, begin):
            if tar < 0:
                return None
            elif tar == 0:
                ans.append(path[:])
            for i in range(begin, length):
                residue = tar - candidates[i]
                if residue < 0:
                    break
                if i > begin and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(residue, i+1)
                path.pop()

        dfs(target, 0)
        return ans


if __name__ == '__main__':
    print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))