from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        work_dict = {word: True for word in wordDict}
        length = len(s)
        memo = {}

        def search(start):
            if start == length:
                return True
            if start in memo:
                return memo[start]

            for end in range(start+1, length+1):
                if s[start:end] in work_dict and search(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        search(0)
        return memo[0]


if __name__ == '__main__':
    print(Solution().wordBreak('aaaaaaa', ['aaa', 'aaaa']))