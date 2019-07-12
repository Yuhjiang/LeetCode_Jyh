"""
基本思路：
1. 采用字符串处理数据
2. 判断正负采用比较
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        minus = (x > 0) - (x < 0)   # 正数返回1，负数返回-1

        result = str(abs(x))[::-1]

        result = minus * int(result)
        if -2 ** 31 <= result <= 2 ** 31 - 1:
            return result
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))
    print(s.reverse(123))
    print(s.reverse(120))
    print(s.reverse(0))
    print(s.reverse(1))