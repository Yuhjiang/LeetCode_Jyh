class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] == match.get(i):
                    stack.pop()
                else:
                    stack.append(i)

        return not stack


if __name__ == '__main__':
    print(Solution().isValid('()'))
    print(Solution().isValid('()[]{}'))
    print(Solution().isValid('(]'))
    print(Solution().isValid('([)]'))
    print(Solution().isValid('{[]}'))