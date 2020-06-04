from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid[0]:
            return 0
        dp = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            dp.append([0] * n)

        def find_path(x, y):
            if dp[x][y]:
                return dp[x][y]
            if x < 1 and y < 1:
                l = grid[x][y]
            elif x >= 1 and y < 1:
                l = find_path(x-1, y) + grid[x][y]
            elif x < 1 and y >= 1:
                l = find_path(x, y - 1) + grid[x][y]
            else:
                l = min(find_path(x-1, y), find_path(x, y-1)) + grid[x][y]
            dp[x][y] = l
            return l
        find_path(m-1, n-1)
        return dp[m-1][n-1]


class NewSolution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j == n-1 and i == m-1:
                    dp[j] = grid[i][j]
                elif j < n-1 and i == m-1:
                    dp[j] = grid[i][j] + dp[j+1]
                elif j == n-1 and i < m-1:
                    dp[j] = grid[i][j] + dp[j]
                else:
                    dp[j] = grid[i][j] + min(dp[j], dp[j+1])
        return dp[0]


class SecondSolution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j == n-1 and i == m-1:
                    grid[i][j] = grid[i][j]
                elif j < n-1 and i == m-1:
                    grid[i][j] += grid[i][j+1]
                elif j == n-1 and i < m-1:
                    grid[i][j] += grid[i+1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i+1][j], grid[i][j+1])
        return grid[0][0]


if __name__ == '__main__':
    print(SecondSolution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))