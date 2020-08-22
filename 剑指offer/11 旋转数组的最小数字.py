from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return -1

        left, right = 0, len(numbers) - 1
        mid = 0

        while numbers[left] >= numbers[right]:
            if right - left == 1:
                mid = right
                break

            mid = (left + right) // 2
            if numbers[mid] == numbers[left] == numbers[right]:
                return self.find_in_order(numbers, left, right)
            if numbers[mid] >= numbers[left]:
                left = mid
            elif numbers[mid] <= numbers[right]:
                right = mid

        return numbers[mid]

    def find_in_order(self, numbers: List[int], left, right):
        res = numbers[left]
        left += 1
        while left <= right:
            if numbers[left] < res:
                res = numbers[left]
                break
            left += 1
        return res


if __name__ == '__main__':
    # print(Solution().minArray([3, 4, 5, 1, 2]))
    # print(Solution().minArray([1, 1, 1, 0, 1]))
    print(Solution().minArray([2, 2, 2, 0, 1]))
    print(Solution().minArray([3, 1]))