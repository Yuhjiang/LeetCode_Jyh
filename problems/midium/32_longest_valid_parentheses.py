class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def is_valid(string):
            stack = []

            for i in string:
                if i == '(':
                    stack.append(i)
                elif stack and i == ')':
                    stack.pop()
                else:
                    return False
            return not stack

        max_count = 0

        for i in range(len(s)):
            for j in range(i+2, len(s)+1, 2):
                if is_valid(s[i:j]):
                    max_count = max_count if max_count > j-i else j-i

        return max_count


class NewSolution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]

        max_count = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i - dp[i-1] >= 2 else 0) + 2
                max_count = max_count if max_count > dp[i] else dp[i]

        return max_count


class ThirdSolution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_count = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_count = max_count if max_count > i-stack[-1] else i-stack[-1]

        return max_count


if __name__ == '__main__':
    print(ThirdSolution().longestValidParentheses("(()))())("))