"""
建立一个空列表
1. 每次添加元素时维护一个最长子字符串
2. 每次碰到重复元素，更新当前的子字符串[next index of repeated char]
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substring = []
        current_substring = []

        for i in s:
            if i not in current_substring:      # 未出现重复元素
                current_substring.append(i)
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
            else:                               # 出现了重复元素
                index = current_substring.index(i)
                current_substring = current_substring[index+1:]
                current_substring.append(i)

        return len(longest_substring)


# if __name__ == '__main__':
#     s = Solution()
#
#     print(s.lengthOfLongestSubstring('abcabcbb'))
#     print(s.lengthOfLongestSubstring('bbbb'))
#     print(s.lengthOfLongestSubstring('pwwkew'))
