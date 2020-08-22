class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += n & 1
            n = n >> 1
        return count


class Solution2:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = (n - 1) & n
        return count


if __name__ == '__main__':
    print(Solution2().hammingWeight(11))