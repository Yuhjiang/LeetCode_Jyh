"""
正则表达式
*匹配前一个字符0次多多次
.匹配任意一个字符
动态规划
参考：https://leetcode.com/problems/regular-expression-matching/discuss/5678/Fast-Python-solution-with-backtracking-and-caching-%2B-DP-solution
"""


class Solution:
    cache = {}  # 保存每一对s，p是否匹配的结果

    def isMatch(self, s: str, p: str) -> bool:
        if (s, p) in self.cache:
            return self.cache[(s, p)]

        if not p:
            return not s

        if p[-1] == '*':
            # 第一种情况，匹配到不到s[-1]，直接从-2开始匹配
            if self.isMatch(s, p[:-2]):
                self.cache[(s, p)] = True
                return True
            # 第二种情况，匹配到了，还能继续匹配0次或多次
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):
                self.cache[(s, p)] = True
                return True
        # 第三种情况，直接匹配单个字符
        if s and (s[-1] == p[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s, p)] = True
            return True
        self.cache[(s, p)] = False
        return False


if __name__ == '__main__':
    test = [['aa', 'a'], ['aa', 'a*'], ['ab', '.*'], ['aab', 'c*a*b'], ['mississippi', 'mis*is*p*.'], ['aaa', 'a*a'], ['aaa', 'aaaa'], ['aaa', 'ab*a*c*a']]
    sol = Solution()

    for t in test:
        print(sol.isMatch(t[0], t[1]))