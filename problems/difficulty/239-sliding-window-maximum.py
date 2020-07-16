from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        length = len(nums)
        if length * k == 0:
            return []
        if k == 1:
            return nums

        def clean_queue(i):
            if dep and dep[0] == i - k:
                dep.popleft()

            while dep and nums[i] > nums[dep[-1]]:
                dep.pop()

        dep = deque()
        max_idx = 0
        for i in range(k):
            clean_queue(i)
            dep.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        ans = [nums[max_idx]]

        for i in range(k, length):
            clean_queue(i)
            dep.append(i)
            ans.append(nums[dep[0]])
        return ans


class NewSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        if length * k == 0:
            return []
        if k == 1:
            return nums

        left = [0 for _ in range(length)]
        right = [0 for _ in range(length)]
        left[0], right[-1] = nums[0], nums[-1]

        for i in range(1, length):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])
            j = length - i - 1
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])

        ans = []
        for i in range(length - k + 1):
            ans.append(max(left[i+k-1], right[i]))

        return ans


if __name__ == '__main__':
    print(NewSolution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    print(NewSolution().maxSlidingWindow([1,3,-1,-3,5,7,6,7], 3))
