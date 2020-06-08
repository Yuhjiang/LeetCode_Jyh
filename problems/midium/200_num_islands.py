from typing import List
import pprint


class Solution:
    def __init__(self):
        self.max_i = 0
        self.max_j = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.max_i = len(grid)
        self.max_j = len(grid[0])
        visited = []
        for i in range(self.max_i):
            temp = [0] * self.max_j
            visited.append(temp)

        num = 0
        for i in range(self.max_i):
            for j in range(self.max_j):
                if visited[i][j]:
                    continue
                if grid[i][j] == '1' and not visited[i][j]:
                    num += 1
                    visited[i][j] = 1
                    self.dfs(i-1, j, grid, visited)
                    self.dfs(i+1, j, grid, visited)
                    self.dfs(i, j-1, grid, visited)
                    self.dfs(i, j+1, grid, visited)
        return num

    def dfs(self, i, j, grid, visited):
        if 0 <= i <= self.max_i-1 and 0 <= j <= self.max_j-1:
            if visited[i][j] or grid[i][j] == '0':
                return None
            visited[i][j] = 1
            self.dfs(i - 1, j, grid, visited)
            self.dfs(i + 1, j, grid, visited)
            self.dfs(i, j - 1, grid, visited)
            self.dfs(i, j + 1, grid, visited)
        else:
            return None


if __name__ == '__main__':
    s = Solution()
    input_str = ['11000', '11000', '00100', '00011']
    g = []
    for i in input_str:
        g.append([j for j in i])

    # g = [["1","1","1"],["0","1","0"],["1","1","1"]]
    print(s.numIslands(g))