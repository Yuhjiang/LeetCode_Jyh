class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        all_s = [str(i) for i in range(1, n+1)]
        s = ''

        def fac(n):
            res = 1
            while n >= 1:
                res *= n
                n -= 1
            return res

        k -= 1
        while n > 0:
            t = fac(n-1)
            i = k // t
            s += all_s[i]
            all_s.pop(i)
            k = k - i * t
            n -= 1

        return s


if __name__ == '__main__':
    print(Solution().getPermutation(3, 3))
    print(Solution().getPermutation(4, 9))