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


if __name__ == '__main__':
    # print(Solution().convert('PAYPALISHIRING', 3))
    print(Solution().convert('ABC', 1))
