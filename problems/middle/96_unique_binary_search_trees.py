class Solution:
    def numTrees(self, n: int) -> int:
        total = [0] * (n+1)
        total[0] = total[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                total[i] += total[j-1] * total[i-j]

        return total[n]


if __name__ == '__main__':
    print(Solution().numTrees(3))