"""
求商
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 1
        minus = 1

        if dividend < 0:
            dividend = - dividend
            minus = -minus
        if divisor < 0:
            divisor = -divisor
            minus = -minus

        if dividend < divisor:
            return 0

        divisor_m_quotient = divisor
        res = 0
        while dividend >= divisor:
            temp = divisor_m_quotient + divisor_m_quotient        # 翻倍
            # print(dividend, temp, quotient, res)
            if temp < dividend:                 # 翻倍之后还能比dividend大，就更新quotient
                quotient += quotient
                divisor_m_quotient = temp
            else:
                dividend -= divisor_m_quotient  # 翻倍之后超了，记录当前商，然后对剩余dividend做重复操作
                res += quotient
                quotient = 1
                divisor_m_quotient = divisor

        res = res * minus

        return res if res <= 2**31-1 else 2**31-1


if __name__ == '__main__':
    s = Solution()
    print(s.divide(2**31, 1))