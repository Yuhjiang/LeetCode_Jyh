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


if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))