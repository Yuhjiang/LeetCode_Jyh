class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n == 0:
            return 1
        elif n == -1:
            return 1 / x
        else:
            tmp = self.myPow(x, n // 2)
            if n % 2 != 0:
                return tmp * tmp * x
            else:
                return tmp * tmp


if __name__ == '__main__':
    print(Solution().myPow(2, 10))
    print(Solution().myPow(2.1, 3))
    print(Solution().myPow(2.1, 1))
    print(Solution().myPow(2.1, 0))
    print(Solution().myPow(2.1, -1))
    print(Solution().myPow(2, -2))