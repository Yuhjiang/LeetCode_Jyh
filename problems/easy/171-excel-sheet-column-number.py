class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            ans = ans * 26 + ord(s[i]) - 64

        return ans


if __name__ == '__main__':
    print(Solution().titleToNumber('A'))
    print(Solution().titleToNumber('AB'))
    print(Solution().titleToNumber('ZY'))