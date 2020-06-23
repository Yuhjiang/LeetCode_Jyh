from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num+1)

        current_square = 1
        last_square = 0
        for i in range(1, num+1):
            if current_square == i:
                dp[i] = 1
                last_square = current_square
                current_square *= 2
            else:
                dp[i] = dp[i-last_square] + 1

        return dp


if __name__ == '__main__':
    print(Solution().countBits(10))