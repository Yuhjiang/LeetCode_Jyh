class Solution:
    def romanToInt(self, s: str) -> int:
        digit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        ans = 0
        length = len(s)
        for i in range(length-1, -1, -1):
            if i < length-1 and digit[s[i]] < digit[s[i+1]]:
                sign = -1
            else:
                sign = 1
            ans += sign * digit[s[i]]

        return ans


if __name__ == '__main__':
    print(Solution().romanToInt('III'))
    print(Solution().romanToInt('IV'))
    print(Solution().romanToInt('IX'))
    print(Solution().romanToInt('LVIII'))
    print(Solution().romanToInt('MCMXCIV'))