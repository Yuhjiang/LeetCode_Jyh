from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        if not matrix or not matrix[0]:
            return found
        rows, columns = len(matrix), len(matrix[0])
        row, col = 0, columns-1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                found = True
                break
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return found


if __name__ == '__main__':
    print(Solution().findNumberIn2DArray([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 5))