from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = m + n - 1
        i = m - 1
        j = n - 1

        while pos >= 0 and i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[pos] = nums2[j]
                j -= 1
            else:
                nums1[pos] = nums1[i]
                i -= 1
            pos -= 1

        if i == -1:
            nums1[:pos+1] = nums2[:j+1]


if __name__ == '__main__':
    nums1 = [4,5,6,0,0,0]
    Solution().merge(nums1, 3, [1, 2, 3], 3)
    print(nums1)