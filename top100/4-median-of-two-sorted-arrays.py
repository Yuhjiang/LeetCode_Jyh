from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        left, right = 0, m

        INFINITY = 2**40

        median1, median2 = 0, 0

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            nums1_im = -INFINITY if i == 0 else nums1[i-1]
            nums1_i = INFINITY if i == m else nums1[i]
            nums2_jm = -INFINITY if j == 0 else nums2[j-1]
            nums2_j = INFINITY if j == n else nums2[j]

            if nums1_im <= nums2_j:
                median1, median2 = max(nums1_im, nums2_jm), min(nums1_i, nums2_j)
                left = i + 1
            else:
                right = i - 1

        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 3], [2]))