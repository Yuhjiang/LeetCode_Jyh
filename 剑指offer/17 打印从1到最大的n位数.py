from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        if n == 0:
            return []

        i = 0
        number = 1
        while i < n:
            i += 1
            number *= 10

        ans = []
        for i in range(1, number):
            ans.append(i)

        return ans


class Solution2:
    def printNumbers(self, n: int) -> List[int]:
        ans = []

        def generate_number(num: List, length: int):
            if length == n:
                ans.append(num)
                return

            for i in range(10):
                num[length] = i
                generate_number(num.copy(), length+1)

        generate_number([0 for i in range(n)], 0)

        return ans


if __name__ == '__main__':
    print(Solution2().printNumbers(2))