"""
寻找最长的字符串相同首字符串
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs == []:
            return ''
        if len(strs) == 1:
            return strs[0]
        prefix = ''
        i = 0
        while True:
            for s in strs:
                if len(s) == i:
                    return prefix
                if s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
            i += 1


if __name__ == '__main__':
    test = [
        # ["flower", "flow", "flight"],
        # ["dog", "racecar", "car"],
        # ['aa', 'a'],
        # ['']
        ['a', 'ac']
    ]
    s = Solution()
    for t in test:
        print(s.longestCommonPrefix(t))