class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        while n > 0:
            t = n % 26
            ans = (chr(64 + t) if t != 0 else 'Z') + ans
            if n == 26:
                break
            n = n // 26

        return ans


if __name__ == '__main__':
    print(Solution().convertToTitle(701))
    print(Solution().convertToTitle(700))
    print(Solution().convertToTitle(26))
    print(Solution().convertToTitle(52))