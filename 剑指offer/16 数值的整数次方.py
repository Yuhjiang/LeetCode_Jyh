class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or n == 0:
            return 1

        flag = 1
        if n < 0:
            flag = -1
            n = -n

        def product(n_):
            if n_ == 1:
                return x
            elif n_ % 2 == 0:
                tmp = self.myPow(x, n_ // 2)
                return tmp * tmp
            else:
                tmp = self.myPow(x, n_ // 2)
                return tmp * tmp * x

        ans = product(n)
        if flag == -1:
            return 1 / ans
        else:
            return ans
