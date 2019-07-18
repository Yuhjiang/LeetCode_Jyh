"""
整数转罗马字
特殊情况
1.I can be placed before V (5) and X (10) to make 4 and 9.
2.X can be placed before L (50) and C (100) to make 40 and 90.
3.C can be placed before D (500) and M (1000) to make 400 and 900.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M'], ['M']]
        romans = ''
        digit = 0
        while num != 0:
            remainder = num % 10
            if remainder <= 3:
                temp = symbols[digit][0] * remainder
            elif remainder == 4:
                temp = symbols[digit][0] + symbols[digit][1]
            elif remainder == 9:
                temp = symbols[digit][0] + symbols[digit][2]
            else:
                temp = symbols[digit][1] + symbols[digit][0] * (remainder - 5)

            num = num // 10
            digit += 1
            romans = temp + romans

        return romans


if __name__ == '__main__':
    s = Solution()
    test = [[3, 'III'], [4, 'IV'], [9, 'IX'], [58, 'LVIII'], [1994, 'MCMXCIV'], [3999, 'MMMCMXCIX']]

    for t in test:
        print(s.intToRoman(t[0]))
        assert s.intToRoman(t[0]) == t[1]