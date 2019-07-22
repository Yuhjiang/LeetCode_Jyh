"""
罗马字转数字
特殊情况
1.I can be placed before V (5) and X (10) to make 4 and 9.
2.X can be placed before L (50) and C (100) to make 40 and 90.
3.C can be placed before D (500) and M (1000) to make 400 and 900.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        res = 0

        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        last = 'I'
        for i in s:
            if symbols[i] < symbols[last]:
                res -= symbols[i]
            else:
                res += symbols[i]
            last = i

        return res


if __name__ == '__main__':
    test = {
        'III': 3, 'IV': 4, 'IX': 9, 'LVIII': 58, 'MCMXCIV': 1994,
    }
    s = Solution()
    for t in test.keys():
        print(s.romanToInt(t))