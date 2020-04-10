"""
判断括号是否闭合
直接用堆栈
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['*']
        valid_brackets = {'(': ')', '{': '}', '[': ']', '*': '*'}
        for char in s:
            if char in valid_brackets:
                stack.append(char)
            else:
                c = stack.pop()
                if char != valid_brackets[c]:
                    return False
        return len(stack) == 1


if __name__ == '__main__':
    test = ["()", "()[]{}", "(]", "([)]", "{[]}", '[]', ']']
    s = Solution()

    for t in test:
        print(s.isValid(t))