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


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('1010', '1011'))