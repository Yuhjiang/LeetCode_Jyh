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


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('pwwkew'))