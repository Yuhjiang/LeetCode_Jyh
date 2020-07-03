class Solution:
    def intToRoman(self, num: int) -> str:
        cnt = 1
        digit = {
            1: ['I', 'V', 'X'],
            2: ['X', 'L', 'C'],
            3: ['C', 'D', 'M'],
            4: ['M']
        }

        def construct(n):
            d = digit[cnt]
            if n == 0:
                return ''
            elif n <= 3:
                return n * d[0]
            elif n == 4:
                return d[0] + d[1]
            elif n == 5:
                return d[1]
            elif 6 <= n <= 8:
                return d[1] + (n-5) * d[0]
            elif n == 9:
                return d[0] + d[2]
            else:
                return d[2]

        ans = ''
        while num:
            tmp = num % 10
            ans = construct(tmp) + ans
            num = num // 10
            cnt += 1

        return ans


if __name__ == '__main__':
    print(Solution().intToRoman(3))
    print(Solution().intToRoman(4))
    print(Solution().intToRoman(9))
    print(Solution().intToRoman(58))
    print(Solution().intToRoman(1994))
