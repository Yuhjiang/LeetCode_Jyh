class Solution:
    def isMatch(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    return i == len(text)
                else:
                    is_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j+1] == '*':
                        return dp(i, j+2) or is_match and dp(i+1, j)
                    else:
                        return is_match and dp(i+1, j+1)
            else:
                return memo[(i, j)]

        return dp(0, 0)


if __name__ == '__main__':
    print(Solution().isMatch('abc', '.*'))