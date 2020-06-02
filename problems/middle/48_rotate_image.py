from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def _rotate(little_matrix, left, right):
            n = right - left
            for i in range(n):
                little_matrix[left][left+i], little_matrix[left+i][right], little_matrix[right][right-i], little_matrix[right-i][left] = \
                    little_matrix[right-i][left], little_matrix[left][left+i], little_matrix[left+i][right], little_matrix[right][right-i]
        left, right = 0, len(matrix) - 1
        while left < right:
            _rotate(matrix, left, right)
            left += 1
            right -= 1


if __name__ == '__main__':
    s = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
    Solution().rotate(s)
    print(s)