from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l, r = 0, len(nums) - 1

        def build_tree(left, right):
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            if left < mid:
                root.left = build_tree(left, mid-1)
            if right > mid:
                root.right = build_tree(mid+1, right)

            return root

        ans = build_tree(l, r)

        return ans


if __name__ == '__main__':
    res = Solution().sortedArrayToBST([-10,-3,0,5,9])
    print(123)