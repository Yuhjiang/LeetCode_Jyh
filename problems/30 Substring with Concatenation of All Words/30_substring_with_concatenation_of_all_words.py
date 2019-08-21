"""
需要优化
在s中寻找由words里单词串联起来的字符串的起始位置
"""


class Solution:
    def findSubstring(self, s: str, words):
        if s == '' or words == []:
            return []
        word_len = len(words[0])
        left, right = 0, word_len * len(words)

        result = []
        while right <= len(s):
            res, state = self.find_indices(s, words.copy(), left, right, word_len)
            if state == 1:
                result.append(res)
            left = res + 1
            right = left + word_len * len(words)

        return result

    @staticmethod
    def find_indices(s, words, left, right, word_len):
        res = left
        print(s[left:right], left)
        while left < right:
            if s[left:left+word_len] in words:
                words.remove(s[left:left+word_len])
                left += word_len
            else:
                return res, 0
        return res, 1


if __name__ == '__main__':
    sol = Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    print(sol.findSubstring(s, words))