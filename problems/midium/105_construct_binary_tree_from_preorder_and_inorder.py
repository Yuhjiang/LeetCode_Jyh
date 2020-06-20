from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index = {n: i for i, n in enumerate(inorder)}

        def build(pre_left: int, pre_right: int, in_left: int, in_right: int):
            if pre_left > pre_right or in_left > in_right:
                return None
            root_pos = pre_left

            in_pos = index[preorder[root_pos]]
            length = in_pos - in_left
            root = TreeNode(preorder[root_pos])
            root.left = build(pre_left+1, pre_left+length, in_left, in_pos-1)
            root.right = build(pre_left+length+1, pre_right, in_pos+1, in_right)

            return root

        max_len = len(preorder)
        return build(0, max_len-1, 0, max_len-1)


if __name__ == '__main__':
    from problems.utils import print_tree
    print_tree(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))