class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_length = 0

        self.max_depth(root)
        return self.max_length

    def max_depth(self, root, deep=0):
        if not root:
            return 0
        else:
            left_max_depth = self.max_depth(root.left, deep)
            right_max_depth = self.max_depth(root.right, deep)
            current_length = left_max_depth + right_max_depth
            if self.max_length < current_length:
                self.max_length = current_length
            return 1 + max(left_max_depth, right_max_depth)


if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.left.left = TreeNode(4)
    r.left.right = TreeNode(5)
    r.right.right = TreeNode(6)

    print(Solution().diameterOfBinaryTree(r))
