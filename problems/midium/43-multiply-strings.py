class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = '0'
        if num1 == '0' or num2 == '0':
            return res

        m, n = len(num1)-1, len(num2)-1
        while n >= 0:
            flag = 0
            tmp = ''
            for _ in range(len(num2) - 1 - n):
                tmp += '0'
            x = ord(num2[n]) - 48
            j = m
            while j >= 0 or flag != 0:
                y = 0 if j < 0 else ord(num1[j]) - 48
                product = (x * y + flag) % 10
                tmp += str(product)
                flag = (x * y + flag) // 10
                j -= 1
            n -= 1
            res = self.add(res, tmp[::-1])
        return res

    def add(self, num1, num2):
        m, n = len(num1)-1, len(num2)-1
        ans = ''
        flag = 0

        while m >= 0 or n >= 0 or flag != 0:
            x = 0 if m < 0 else ord(num1[m]) - 48
            y = 0 if n < 0 else ord(num2[n]) - 48
            sum = (x + y + flag) % 10
            ans = str(sum) + ans
            flag = (x + y + flag) // 10
            m -= 1
            n -= 1

        return ans


if __name__ == '__main__':
    print(Solution().multiply('123', '456'))
