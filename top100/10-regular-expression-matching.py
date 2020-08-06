class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if j == len(p):
                return i == len(s)
            if (i, j) in memo:
                return memo[(i, j)]
            is_match = i < len(s) and p[j] in [s[i], '.']
            if j < len(p) - 1 and p[j+1] == '*':
                res = is_match and dp(i+1, j) or dp(i, j+2)
            else:
                res = is_match and dp(i+1, j+1)
            memo[(i, j)] = res
            return res

        return dp(0, 0)


if __name__ == '__main__':
    print(Solution().isMatch('aa', 'a'))
    print(Solution().isMatch('aa', 'a*'))
    print(Solution().isMatch('ab', '.*'))
    print(Solution().isMatch('aab', 'c*a*b'))