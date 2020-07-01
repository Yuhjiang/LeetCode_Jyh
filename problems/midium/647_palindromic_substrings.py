class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        dp = [[False for _ in range(length)] for _ in range(length)]

        for l in range(length):
            for i in range(length):
                j = i + l
                if j >= length:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        count = 0
        for i in dp:
            for j in i:
                if j:
                    count += 1
        return count


if __name__ == '__main__':
    print(Solution().countSubstrings('aaa'))
    print(Solution().countSubstrings('abc'))
    print(Solution().countSubstrings('abccba'))