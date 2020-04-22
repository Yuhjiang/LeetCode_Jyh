class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        new_root = TreeNode(root.val)

        self.preorder_traversal(root, new_root)

        return new_root

    def preorder_traversal(self, root, new_root):
        if root.left:
            new_root.right = TreeNode(root.left.val)
            self.preorder_traversal(root.left, new_root.right)
        if root.right:
            new_root.left = TreeNode(root.right.val)
            self.preorder_traversal(root.right, new_root.left)

    def preorder(self, root):
        if root.left:
            self.preorder(root.left)
        if root.right:
            self.preorder(root.right)


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    s = Solution()
    s.preorder(s.invertTree(root))

