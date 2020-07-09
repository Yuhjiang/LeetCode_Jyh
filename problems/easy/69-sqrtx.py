class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, ans = 0, x, -1

        while left <= right:
            mid = (left + right) // 2
            tmp = mid * mid
            if tmp <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


if __name__ == '__main__':
    print(Solution().mySqrt(9))