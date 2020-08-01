class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31

        ans = 0
        flag = 1 if x > 0 else -1
        x = abs(x)
        while x > 0:
            ans = ans * 10 + x % 10
            x //= 10

        ans = flag * ans

        if ans > MAX or ans < MIN:
            return 0
        else:
            return ans


if __name__ == '__main__':
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
    print(Solution().reverse(0))