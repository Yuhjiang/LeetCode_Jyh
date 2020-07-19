class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0

        tmp = 5
        while tmp <= n:
            ans += n // tmp
            tmp *= 5

        return ans


if __name__ == '__main__':
    # print(Solution().trailingZeroes(3))
    # print(Solution().trailingZeroes(5))
    # print(Solution().trailingZeroes(1))
    # print(Solution().trailingZeroes(8))
    print(Solution().trailingZeroes(25))