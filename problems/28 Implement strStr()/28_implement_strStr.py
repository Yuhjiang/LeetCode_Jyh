"""
在haystack里寻找needle
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left, right = 0, len(needle) - 1
        res = -1
        while right < len(haystack):
            if haystack[left:right+1] == needle:
                res = left
                break
            else:
                left += 1
                right += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.strStr('aaaaa', 'bba'))