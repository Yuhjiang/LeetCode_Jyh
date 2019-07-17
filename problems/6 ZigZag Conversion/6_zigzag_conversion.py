"""
Z字型弯曲字符串
1. 第一列竖着n个字符
2. 斜着n-2个字符
3. 第n列竖着n个字符
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = []
        for _ in range(numRows):
            res.append([])

        if numRows == 1:
            return s

        loop = numRows + numRows - 2    # n个竖的，n-2个斜的
        for i, s in enumerate(s):
            j = i % loop     # 用于定位
            # 0到n-1可以直接在相应位置
            if 0 <= j <= numRows - 1:
                res[j].append(s)
            # n到2n - 3 需要再确定位置
            else:
                res[numRows - j % numRows - 2].append(s)

        result = ''
        for i in range(numRows):
            result += ''.join(res[i])
        return result


if __name__ == '__main__':
    sol = Solution()
    result = sol.convert('A', 1)
    print(result)