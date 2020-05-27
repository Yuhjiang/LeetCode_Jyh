class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count


if __name__ == '__main__':
    print(Solution().hammingWeight(11))