from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k + 1
        heapq.heapify(nums)
        t = nums[0]
        for i in range(k):
            t = heapq.heappop(nums)
        return t


class NewSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick(nums, 0, len(nums)-1, len(nums)-k)

    def quick(self, nums, left, right, index):
        p = self.partition(nums, left, right)

        if p == index:
            return nums[p]
        else:
            if p < index:
                return self.quick(nums, p+1, right, index)
            else:
                return self.quick(nums, left, p-1, index)

    def partition(self, nums: List[int], left: int, right: int):
        middle = (left + right) // 2
        pivot = nums[middle]
        nums[right], nums[middle] = nums[middle], nums[right]
        boundary = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[boundary], nums[i] = nums[i], nums[boundary]
                boundary += 1
        nums[boundary], nums[right] = nums[right], nums[boundary]
        return boundary


if __name__ == '__main__':
    # print(NewSolution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
    print(NewSolution().findKthLargest(
        [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 20))