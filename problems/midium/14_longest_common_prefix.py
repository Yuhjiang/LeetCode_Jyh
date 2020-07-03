from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        ans = ''

        min_length = 1000
        for i in strs:
            min_length = min(min_length, len(i))

        pos = 0
        while True:
            if pos >= min_length:
                return ans
            tmp = strs[0]
            for i in strs[1:]:
                if tmp[pos] != i[pos]:
                    return ans
            ans += tmp[pos]
            pos += 1
        return ans


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))
    print(Solution().longestCommonPrefix(["dog"]))
    print(Solution().longestCommonPrefix(['']))