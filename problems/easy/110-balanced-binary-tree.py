class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def pre_order_traversal(tree: TreeNode):
            if tree:
                height_left, balanced_left = pre_order_traversal(tree.left)
                height_right, balanced_right = pre_order_traversal(tree.right)
                if not balanced_left or not balanced_right:
                    return 0, False
                if abs(height_left - height_right) >= 2:
                    return 0, False
                return max(height_left, height_right) + 1, True
            else:
                return 0, True

        return pre_order_traversal(root)[1]


if __name__ == '__main__':
    pass