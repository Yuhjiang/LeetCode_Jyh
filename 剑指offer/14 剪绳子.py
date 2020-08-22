class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        products = [0 for _ in range(n+1)]
        products[0], products[1], products[2], products[3] = 0, 1, 2, 3

        for i in range(4, n+1):
            max_ = 0

            for j in range(1, i // 2 + 1):
                max_ = max(max_, products[j] * products[i-j])

            products[i] = max_

        return max(products)


if __name__ == '__main__':
    print(Solution().cuttingRope(10))