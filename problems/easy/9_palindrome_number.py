class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        length = len(x)
        for i in range(length // 2):
            if x[i] != x[length-1-i]:
                return False
        return True


class NewSolution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False

        last = 0
        pre = x
        while last < pre:
            last = last * 10 + pre % 10
            pre = pre // 10

        return last == pre or last // 10 == pre


if __name__ == '__main__':
    print(NewSolution().isPalindrome(121))