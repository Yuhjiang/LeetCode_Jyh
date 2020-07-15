from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_ind = 0

        total = n * n
        cnt = 1
        i, j = 0, 0
        while cnt <= total:
            matrix[i][j] = cnt
            cnt += 1

            next_i, next_j = directions[direction_ind][0] + i,\
                             directions[direction_ind][1] + j
            if not (0 <= next_i < n and 0 <= next_j < n and not matrix[next_i][next_j]):
                direction_ind = (direction_ind + 1) % 4
            i, j = directions[direction_ind][0] + i,\
                   directions[direction_ind][1] + j

        return matrix


if __name__ == '__main__':
    print(Solution().generateMatrix(1))
    print(Solution().generateMatrix(2))
    print(Solution().generateMatrix(3))
    print(Solution().generateMatrix(4))