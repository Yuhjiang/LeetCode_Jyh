"""
生成格式化的括号串
1.采用动态规划的方法，n=2可由n=1推导出
2.需要及时去除重复的括号串
"""


class Solution:
    def generateParenthesis(self, n: int):
        res = ['']
        for _ in range(n):
            res = self.generatefrom(res)
        return res

    def generatefrom(self, src):
        res = []
        for s in src:
            # '( ( ) )'
            for i in range(len(s)+1):
                res.append(s[:i] + '()' + s[i:])

        # 去重
        return list(set(res))


if __name__ == '__main__':
    s = Solution()
    import pprint

    pprint.pprint(s.generateParenthesis(3))