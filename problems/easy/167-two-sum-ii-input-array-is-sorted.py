from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                break

        return [left+1, right+1]




if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15], 9))
    print(Solution().twoSum([2,7,11,15], 17))
    print(Solution().twoSum([1], 17))
