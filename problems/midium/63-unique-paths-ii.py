from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        if not obstacleGrid[0]:
            return 1
        if obstacleGrid[0][0] == 1:
            return 0

        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0

        def dfs(i, j):
            if obstacleGrid[i][j] == 1:
                return 0
            if i > 0:
                dp[i][j] = dp[i][j] + dfs(i-1, j)
            if j > 0:
                dp[i][j] = dp[i][j] + dfs(i, j-1)
            return dp[i][j]

        return dfs(row-1, col-1)


class NewSolution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(col)]

        dp[0] = 1 if obstacleGrid[0][0] != 1 else 0

        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue

                if j - 1 >= 0 and obstacleGrid[i][j-1] == 0:
                    dp[j] += dp[j-1]

        return dp[col-1]

if __name__ == '__main__':
    print(NewSolution().uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))
    # print(Solution().uniquePathsWithObstacles([
    #   [1], [0]
    # ]))