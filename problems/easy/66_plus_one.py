from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pos = len(digits) - 1
        if pos == 0 and digits[0] == 0:
            return [1]

        curr = digits[pos] + 1
        if curr >= 10:
            digits[pos] = curr - 10
            flag = 1
        else:
            digits[pos] = curr
            flag = 0
        pos -= 1
        while pos >= 0:
            curr = digits[pos] + flag
            if curr >= 10:
                digits[pos] = curr - 10
                flag = 1
            else:
                digits[pos] = curr
                flag = 0
            pos -= 1
        if flag == 1:
            digits.insert(0, flag)
        return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([0]))