from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]

        ans = []

        def is_valid(row, col):
            # 检查列是否有皇后
            for i in range(n):
                if board[i][col] == 'Q':
                    return False

            # 检查右上方是否有皇后
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i, j = i - 1, j + 1

            # 检查左上方是否有皇后
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i, j = i - 1, j - 1
            return True

        def backtrack(row):
            if row == n:
                tmp = [''.join(i) for i in board]
                ans.append(tmp)
                return

            for col in range(n):
                if not is_valid(row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

        backtrack(0)

        return ans


if __name__ == '__main__':
    import pprint
    pprint.pprint(Solution().solveNQueens(4))