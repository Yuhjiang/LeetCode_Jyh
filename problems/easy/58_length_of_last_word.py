class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(' ')
        return len(words[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord(' a '))