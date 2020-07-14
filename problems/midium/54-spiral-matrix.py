from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height, width = len(matrix), len(matrix[0])
        total = height * width
        visited = [[False for _ in range(width)] for _ in range(height)]

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_ind = 0

        ans = [0 for _ in range(total)]
        i, j = 0, 0
        for k in range(total):
            ans[k] = matrix[i][j]
            visited[i][j] = True
            next_i, next_j = i + directions[direction_ind][0],\
                             j + directions[direction_ind][1]
            if not (0 <= next_i < height and 0 <= next_j < width and not visited[next_i][next_j]):
                direction_ind = (direction_ind + 1) % 4
            i, j = i + directions[direction_ind][0], \
                   j + directions[direction_ind][1]

        return ans


if __name__ == '__main__':
    print(Solution().spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
    print(Solution().spiralOrder(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
    ))
    print(Solution().spiralOrder(
        [
            [7], [9], [6]
        ]
    ))
    print(Solution().spiralOrder(
        [
            []
        ]
    ))
