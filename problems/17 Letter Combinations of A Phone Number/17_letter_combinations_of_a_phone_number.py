"""
将键盘上的数字对应的字母组合起来
"""


class Solution:
    def letterCombinations(self, digits: str):
        if digits == '':
            return []

        digit2alpha = 'abcdefghijklmnopqrstuvwxyz'

        pos = [0, 3, 6, 9, 12, 15, 19, 22, 26]

        res = ['']
        for d in digits:
            start, end = pos[int(d) - 2], pos[int(d) - 1]
            temp = []
            for r in res:
                temp += [r + s for s in digit2alpha[start:end]]
            res = temp
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('7'))