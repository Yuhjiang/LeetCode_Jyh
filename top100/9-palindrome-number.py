class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0:
            return False

        y = 0
        while y < x:
            y = y * 10 + x % 10
            x = x // 10

        return x == y or x == y // 10


if __name__ == '__main__':
    # print(Solution().isPalindrome(1221))
    print(Solution().isPalindrome(10))