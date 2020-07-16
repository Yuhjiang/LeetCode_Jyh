from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        matrix = [[False for _ in range(n)] for _ in range(n)]

        def is_valid(row, col):
            # 同列
            for i in range(0, row):
                if matrix[i][col]:
                    return False

            # 右上
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if matrix[i][j]:
                    return False
                i, j = i - 1, j + 1

            # 左上
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if matrix[i][j]:
                    return False
                i, j = i - 1, j - 1

            return True

        self.count = 0

        def backtrack(row):
            if row == n:
                self.count += 1

            for col in range(n):
                if not is_valid(row, col):
                    continue

                matrix[row][col] = True
                backtrack(row+1)
                matrix[row][col] = False
        backtrack(0)

        return self.count


if __name__ == '__main__':
    print(Solution().totalNQueens(8))