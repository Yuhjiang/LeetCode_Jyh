from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_container = 0
        left, right = 0, len(height) - 1
        while left < right:
            max_container = max(min(height[left], height[right]) * (right - left), max_container)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_container


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
