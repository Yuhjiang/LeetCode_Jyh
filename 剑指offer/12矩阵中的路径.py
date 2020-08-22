from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False

        length = len(word)
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(row, col, pos):
            if pos == length:
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            if board[row][col] == word[pos] and not visited[row][col]:
                visited[row][col] = True
                res = dfs(row-1, col, pos+1) or dfs(row+1, col, pos+1) or dfs(row, col-1, pos+1) or dfs(row, col+1, pos+1)
                visited[row][col] = False
                return res
            else:
                return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    print(Solution().exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        'ABCCED'
    ))

    print(Solution().exist(
        [["a", "b"], ["c", "d"]],
        'abcd'
    ))