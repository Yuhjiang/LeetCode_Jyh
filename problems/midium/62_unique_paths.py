class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            dp.append([0] * n)

        def find_path(x, y):
            if dp[x][y]:
                return dp[x][y]
            if x < 1 and y < 1:
                l = 1
            elif x >= 1 and y < 1:
                l = find_path(x-1, y)
            elif x < 1 and y >= 1:
                l = find_path(x, y-1)
            else:
                l = find_path(x-1, y) + find_path(x, y-1)
            dp[x][y] = l
            return l

        find_path(m-1, n-1)
        return dp[m-1][n-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 2))