class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if not m or not n:
            return 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        return self.move(0, 0, visited, m, n, k)

    def move(self, row, col, visited, m, n, k):
        count = 0
        if self.check(row, col, m, n, visited, k):
            visited[row][col] = True
            count = 1 +\
                       self.move(row-1, col, visited, m, n, k) +\
                       self.move(row+1, col, visited, m, n, k) + \
                       self.move(row, col-1, visited, m, n, k) + \
                       self.move(row, col+1, visited, m, n, k)
        return count

    def get_sum(self, num):
        ans = 0
        while num:
            ans = ans + num % 10
            num //= 10

        return ans

    def check(self, row, col, rows, cols, visited, k):
        if 0 <= row < rows and 0 <= col < cols and not visited[row][col]:
            return self.get_sum(row) + self.get_sum(col) <= k
        return False


if __name__ == '__main__':
    # print(Solution().movingCount(2, 3, 1))
    # print(Solution().movingCount(3, 1, 0))
    print(Solution().movingCount(3, 2, 17))