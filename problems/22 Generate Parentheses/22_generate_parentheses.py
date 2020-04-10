"""
生成格式化的括号串
1.采用动态规划的方法，n=2可由n=1推导出
2.需要及时去除重复的括号串
"""
from typing import List


class Solution:
    """
    深度优先搜索
    """
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(current_str, left, right):
            """
            递归搜索
            :param current_str: 当前节点的
            :param left: 左节点可用数量
            :param right: 右节点可用数量
            :return:
            """
            if left == 0 and right == 0:
                res.append(current_str)
                return
            if right < left:
                return
            else:
                if left > 0:
                    # 这里要注意，不能把值的修改放到外面，否则会污染下面的逻辑
                    dfs(current_str + '(', left - 1, right)
                if right > 0:
                    dfs(current_str + ')', left, right - 1)
        dfs('', n, n)
        return res


class DpSolution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp_result = [[] for _ in range(n + 1)]
        dp_result[0] = ['']

        for i in range(1, n + 1):
            curr = []
            for j in range(i):
                left = dp_result[j]
                right = dp_result[i - j - 1]
                for l in left:
                    for r in right:
                        curr.append('({}){}'.format(l, r))
            dp_result[i] = curr
        return dp_result[n]


if __name__ == '__main__':
    s = DpSolution()
    import pprint

    pprint.pprint(s.generateParenthesis(3))