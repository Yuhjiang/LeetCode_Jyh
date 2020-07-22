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


class NewSolution:
    def longestPalindrome(self, s: str) -> str:
        max_s = ''
        for i in range(len(s)):
            s1 = self.is_palindrome(s, i, i)
            if len(s1) > len(max_s):
                max_s = s1
            if i < len(s) - 1:
                s2 = self.is_palindrome(s, i, i+1)
                if len(s2) > len(max_s):
                    max_s = s2

        return max_s

    def is_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]


if __name__ == '__main__':
    print(NewSolution().longestPalindrome("babad"))
    print(NewSolution().longestPalindrome("cbbd"))