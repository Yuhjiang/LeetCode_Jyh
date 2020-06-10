class Solution:
    def reverse(self, x: int) -> int:
        minus = x < 0
        x = abs(x)
        num = 0
        while x:
            num = num * 10 + x % 10
            x //= 10

        num = num if not minus else -1 * num
        if num < -2**31 or num > 2**31-1:
            return 0
        else:
            return num


if __name__ == '__main__':
    print(Solution().reverse(120))