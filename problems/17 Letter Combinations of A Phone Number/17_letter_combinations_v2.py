class Solution:
    def letterCombinations(self, digits: str):
        if '' == digits:
            return []

        digit2alpha = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        from functools import reduce
        return reduce(lambda acc, digit: [x + y for x in acc for y in digit2alpha[digit]], digits, [''])


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('7'))