"""
https://zhuanlan.zhihu.com/p/70654378
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        imin, imax = 0, m
        i = j = 0
        while imin <= imax:      # 二分法查找i
            i = (imin + imax) // 2  # i, j是划分nums1，nums2的位置的index，即i + j = m - i + n - j + 1
            j = (m + n + 1) // 2 - i
            if i > 0 and nums1[i - 1] > nums2[j]:   # i过大
                imax = i - 1
            elif i < m and nums1[i] < nums2[j - 1]:    # i过小
                imin = i + 1
            else:
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return float(max_left)

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return float((max_left + min_right) / 2)


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([3, 4], [1, 2]))