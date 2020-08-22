from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_index = {x: i for i, x in enumerate(inorder)}

        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right or in_left > in_right:
                return None

            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            pos = inorder_index[preorder[pre_left]]
            length = pos - in_left
            root.left = build(pre_left+1, pre_left+length, in_left, pos-1)
            root.right = build(pre_left+length+1, pre_right, pos+1, in_right)

            return root

        return build(0, len(preorder)-1, 0, len(inorder)-1)


if __name__ == '__main__':
    print(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))