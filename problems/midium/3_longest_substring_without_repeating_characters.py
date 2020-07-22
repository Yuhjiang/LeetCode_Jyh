class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_dict = {}
        max_length = 0

        left = 0
        for right, ch in enumerate(s):
            if ch in s_dict:
                left = max(left, s_dict[ch] + 1)
            s_dict[ch] = right
            print(ch, left, right)
            if max_length < (right - left + 1):
                max_length = right - left + 1
        return max_length


class NewSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        memo = {}
        max_len = 0
        left, right = 0, 0

        while right < len(s):
            if s[right] not in memo:
                memo[s[right]] = right
            else:
                left = max(memo[s[right]] + 1, left)
                memo[s[right]] = right

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len


if __name__ == '__main__':
    print(NewSolution().lengthOfLongestSubstring('pwwkew'))
    print(NewSolution().lengthOfLongestSubstring("abcabcbb"))
    print(NewSolution().lengthOfLongestSubstring("bbbbb"))
    print(NewSolution().lengthOfLongestSubstring("tmmzuxt"))
