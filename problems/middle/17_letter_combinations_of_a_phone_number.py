from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
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
        result = ['']
        for i in digits:
            temp = []
            for n in digit2alpha[i]:
                for i in result:
                    temp.append(i + n)
            result = temp
        return result


class NewSolution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        output = []

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for i in digit2alpha[next_digits[0]]:
                    backtrack(combination + i, next_digits[1:])

        backtrack('', digits)

        return output


if __name__ == '__main__':
    print(NewSolution().letterCombinations("23"))