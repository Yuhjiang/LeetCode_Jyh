"""
盛水最多的容器
找出两条线(i, ai), (j, aj)使得container((j - i) * min(ai, aj))最大
从左右两边逼近，保证j-i最大
证明：
current_water = (j - j) * min(ai, aj)
w为寻找时current_water变大的区域，只能是i或j其中小者向另一者靠近
"""


class Solution:
    def maxArea(self, height) -> int:
        i = 0                    # 左边的线
        j = len(height) - 1      # 右边的线
        most_water = 0
        while i != j:
            current_water = (j - i) * min(height[i], height[j])
            if current_water > most_water:
                most_water = current_water
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return most_water


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))