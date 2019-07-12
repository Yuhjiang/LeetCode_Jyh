"""
判断int是否为回文，不采用字符串
1. 末尾0和负数直接淘汰
2. 利用list存储数据
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x >= 10 and x % 10 == 0):  # -123 or 120
            return False

        x_list = []
        temp = x
        while temp:
            x_list.append(temp % 10)
            temp = temp // 10

        for i in range(len(x_list) // 2):
            if x_list[i] != x_list[-(i+1)]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(1))
    print(s.isPalindrome(10))