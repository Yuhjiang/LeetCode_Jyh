from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                new_list.append(nums1.pop(0))
            else:
                new_list.append(nums2.pop(0))
        if nums1:
            new_list.extend(nums1)
        if nums2:
            new_list.extend(nums2)

        length = len(new_list)
        if length % 2 == 0:
            return (new_list[length // 2] + new_list[length // 2 - 1]) / 2
        else:
            return new_list[length // 2]


class LogSolution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        i = (0 + m) // 2
        while True:
            j = (m + n + 1) // 2 - i
            if i < m and nums2[j-1] > nums1[i]:
                i += 1
            elif i > 0 and nums2[j] < nums1[i-1]:
                i -= 1
            else:
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_left

                if i == m:
                    max_right = nums2[j]
                elif j == n:
                    max_right = nums1[i]
                else:
                    max_right = min(nums1[i], nums2[j])
                return (max_right + max_left) / 2


if __name__ == '__main__':
    print(LogSolution().findMedianSortedArrays([1, 2], [3, 4]))
