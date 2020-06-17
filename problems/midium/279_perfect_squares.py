from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        sqrt_n = int(sqrt(n))
        sqrt_set = {x * x for x in range(1, sqrt_n+1)}
        dp = {}
        for i in range(1, n+1):
            if i in sqrt_set:
                dp[i] = 1
            else:
                for j in range(i // 2, i):
                    # print(i, j)
                    if dp.get(i):
                        tmp = dp[j] + dp[i-j]
                        dp[i] = tmp if tmp < dp[i] else dp[i]
                    else:
                        dp[i] = dp[j] + dp[i-j]

        return dp[n]


class NewSolution:
    def numSquares(self, n: int) -> int:
        square_nums = {x * x for x in range(1, int(sqrt(n))+1)}

        def is_divided_by(num, count):
            if count == 1:
                return num in square_nums

            for k in square_nums:
                if is_divided_by(num-k, count-1):
                    return True
            return False

        for count in range(1, n+1):
            if is_divided_by(n, count):
                return count


if __name__ == '__main__':
    print(NewSolution().numSquares(13))