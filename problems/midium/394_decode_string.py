class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != ']':
                stack.append(i)
            else:
                tmp = ''
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                stack.pop()
                count = ''
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count

                count = int(count)
                tmp = count * tmp
                for j in tmp:
                    stack.append(j)

        return ''.join(stack)


if __name__ == '__main__':
    print(Solution().decodeString("3[a]2[bc]"))
