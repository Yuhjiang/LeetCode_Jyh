class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]

        cnt = 0
        for i in s:
            if cnt < numRows:
                res[cnt % numRows].append(i)
            else:
                res[2 * numRows-cnt-2].append(i)
            cnt += 1
            if cnt >= 2 * numRows - 2:
                cnt = 0

        result = ''.join([''.join(i) for i in res])
        return result


class NewSolution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        flag = 1
        pos = 0

        for i in range(len(s)):
            ans[pos].append(s[i])
            if numRows == 1:
                flag = 0
            elif pos == numRows - 1:
                flag = -1
            elif pos == 0:
                flag = 1

            pos += flag

        return ''.join([''.join(i) for i in ans])


if __name__ == '__main__':
    print(NewSolution().convert('PAYPALISHIRING', 3))
    print(NewSolution().convert('PAYPALISHIRING', 4))      # "PINALSIGYAHRPI"
    print(NewSolution().convert('ABC', 1))
