class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        INFINITY = 1000000007
        pre1, pre2 = 0, 1
        ans = 0
        for i in range(2, n+1):
            ans = pre1 + pre2
            pre1, pre2 = pre2, ans
        if ans > INFINITY:
            ans = ans % INFINITY
        return ans