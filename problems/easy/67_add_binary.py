class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        a_len, b_len = len(a), len(b)
        if a_len < b_len:
            a, b = b, a
            a_len, b_len = b_len, a_len
        a_num = [int(s) for s in a]
        b_num = [int(s) for s in b]

        pos = -1
        flag = 0
        while pos >= -b_len:
            curr = a_num[pos] + b_num[pos] + flag
            if curr >= 2:
                flag = 1
                res = str(curr - 2) + res
            else:
                flag = 0
                res = str(curr) + res
            pos -= 1
        if a_len > b_len:
            while pos >= -a_len:
                curr = a_num[pos] + flag
                if curr >= 2:
                    flag = 1
                    res = str(curr - 2) + res
                else:
                    flag = 0
                    res = str(curr) + res
                pos -= 1
        if flag:
            res = '1' + res
        return res


class NewSolution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        if len(a) > len(b):
            a, b = b, a
        a = a[::-1]
        b = b[::-1]

        plus = 0
        for i in range(len(a)):
            num, plus = self.add(a[i], b[i], plus)
            res.append(num)

        for j in range(len(a), len(b)):
            num, plus = self.add('0', b[j], plus)
            res.append(num)
        if plus:
            res.append(plus)

        return ''.join([str(s) for s in res[::-1]])

    def add(self, a: str, b: str, plus: int):
        if plus:
            if a == '1' and b == '1':
                return 1, 1
            elif a == '0' and b == '0':
                return 1, 0
            else:
                return 0, 1
        else:
            if a == '1' and b == '1':
                return 0, 1
            elif a == '0' and b == '0':
                return 0, 0
            else:
                return 1, 0


if __name__ == '__main__':
    s = NewSolution()
    print(s.addBinary('11', '1'))