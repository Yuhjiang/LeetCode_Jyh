from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 1
        i = len(digits) - 1

        while i >= 0:
            num = digits[i] + flag
            if num == 10:
                flag = 1
                num = 0
            else:
                flag = 0
            digits[i] = num
            i -= 1
        if flag:
            digits = [1] + digits[:]
        return digits


if __name__ == '__main__':
    print(Solution().plusOne([9, 9, 9, 9]))