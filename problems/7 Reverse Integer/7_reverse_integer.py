"""
基本思路：
1. 判断是否是负数，然后转为绝对值
2. 以10取余操作，如果余数为0，说明末尾是0，不操作
3. 溢出返回0
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        minus = 1

        if x < 0:
            minus = -1
            x = abs(x)

        while x != 0:
            remainder = x % 10
            y = y * 10 + remainder
            x = x // 10

        y *= minus
        if y < -2 ** 31 or y > 2 ** 31 - 1:
            return 0

        return y

