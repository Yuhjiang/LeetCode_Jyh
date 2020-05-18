class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_s = ''
        for i in range(len(s)):
            current_s = self.find_longest(s, i, i)
            if len(longest_s) < len(current_s):
                longest_s = current_s
            current_s = self.find_longest(s, i, i+1)
            if len(longest_s) < len(current_s):
                longest_s = current_s
        return longest_s

    def find_longest(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]


if __name__ == '__main__':
    print(Solution().longestPalindrome("b"))