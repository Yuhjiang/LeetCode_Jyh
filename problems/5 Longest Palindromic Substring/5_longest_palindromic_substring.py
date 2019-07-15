"""
寻找最长的回文字符串
1. 奇数长度和偶数长度回文寻找方式不同
2. left,right作为回文中点，随着i逐渐向后移动，并以此为基点寻找最长回文串
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_s = ''      # 保存最长回文串
        window_length = 1

        for i in range(len(s)):
            # 奇数长度
            current_s = self.find_longest(s, i, i)
            if len(current_s) > len(longest_s):
                longest_s = current_s
            current_s = self.find_longest(s, i, i+1)
            if len(current_s) > len(longest_s):
                longest_s = current_s

        return longest_s

    @staticmethod
    def find_longest(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('bananas'))
    print(s.longestPalindrome('babad'))
    print(s.longestPalindrome('ccb'))
    print(s.longestPalindrome('cbbd'))
    print(s.longestPalindrome('aa'))
    print(s.longestPalindrome('aaaabaaa'))
