class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        flag = 1
        if dividend < 0:
            flag = -1 * flag
            dividend = -dividend
        if divisor < 0:
            flag = -1 * flag
            divisor = -divisor

        multi = 1
        pre = divisor
        while divisor <= dividend:
            ans += multi
            tmp = dividend - pre - pre
            if tmp <= divisor:
                multi = 1
                dividend -= divisor
                pre = divisor
            else:
                multi += multi
                dividend = tmp
                pre = pre + pre

        ans = ans * flag
        if ans < -2147483647:
            ans = -2147483647
        elif ans > 2147483648:
            ans = 2147483647
        return ans


if __name__ == '__main__':
    # print(Solution().divide(-2147483648, 3))
    # print(Solution().divide(7, -3))
    # print(Solution().divide(10, 3))
    print(Solution().divide(-2147483648, 1))