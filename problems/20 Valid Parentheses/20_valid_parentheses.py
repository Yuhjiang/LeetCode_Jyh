"""
判断括号是否闭合
直接用堆栈
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_brackets = [('(', ')'), ('{', '}'), ('[', ']')]
        for char in s:
            if not stack:
                stack.append(char)
                continue

            if (stack[-1], char) in valid_brackets:
                stack = stack[:-1]
            else:
                stack.append(char)
        return stack == []


if __name__ == '__main__':
    test = ["()", "()[]{}", "(]", "([)]", "{[]}", '[]']
    s = Solution()

    for t in test:
        print(s.isValid(t))