class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        count = 0
        while res:
            if res & 1:
                count += 1
            res = res >> 1
        return count


if __name__ == '__main__':
    print(Solution().hammingDistance(1, 4))