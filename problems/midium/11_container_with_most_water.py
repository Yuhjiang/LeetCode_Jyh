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


class NewSolution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    print(NewSolution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
