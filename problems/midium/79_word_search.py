from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = []
        for i in range(m):
            visited.append([0] * n)

        possible = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    possible.append([i, j])

        def dfs(x, y, new_word):
            if not new_word:
                return True
            if x < 0 or x >= m:
                return False
            if y < 0 or y >= n:
                return False
            if visited[x][y]:
                return False
            if board[x][y] == new_word[0]:
                visited[x][y] = 1
                result = dfs(x - 1, y, new_word[1:]) or \
                         dfs(x, y - 1, new_word[1:]) or \
                         dfs(x + 1, y, new_word[1:]) or \
                         dfs(x, y + 1, new_word[1:])
                visited[x][y] = 0
                return result
            else:
                return False

        for pos in possible:
            if dfs(pos[0], pos[1], word):
                return True

        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    # ABCB
    print(Solution().exist(board, 'ABCCED'))
