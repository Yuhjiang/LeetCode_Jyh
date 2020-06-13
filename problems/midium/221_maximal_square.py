from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        max_x = len(matrix)
        max_y = len(matrix[0])

        dp = [[0 for _ in range(max_y)] for _ in range(max_x)]
        max_size = 0
        for x in range(max_x):
            for y in range(max_y):
                if matrix[x][y] == '1':
                    if x == 0 or y == 0:
                        dp[x][y] = 1
                    else:
                        dp[x][y] = min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1]) + 1
                    max_size = max_size if max_size > dp[x][y] else dp[x][y]
        return max_size * max_size


if __name__ == '__main__':
    # print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(Solution().maximalSquare([["1","1","0","1"],["1","1","0","1"],["1","1","1","1"]]))