class Solution:
    def replaceSpace(self, s: str) -> str:
        ans = [''] * len(s) * 3

        pos = 0
        for i in s:
            if i != ' ':
                ans[pos] = i
            else:
                ans[pos] = '%20'
            pos += 1

        return ''.join(ans[:pos])


if __name__ == '__main__':
    print(Solution().replaceSpace('We are happy.'))
    print(Solution().replaceSpace(''))
    print(Solution().replaceSpace(' '))