# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.height = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.front(root, 0)
        return self.height

    def front(self, root, height=1):
        if not root:
            return
        if self.height < height:
            self.height = height
        if root.left:
            self.front(root.left, height=height+1)
        if root.right:
            self.front(root.right, height=height+1)


class NewSolution:
    def maxDepth(self, root: TreeNode) -> int:
        self.depth = 0

        return self.depth

    def preorder_traversal(self, root, height):
        if root:
            height += 1
            self.depth = max(height, self.depth)
            self.preorder_traversal(root.left, height)
            self.preorder_traversal(root.right, height)


if __name__ == '__main__':
    from utils import create_tree, print_tree
    tree = create_tree([3,9,20, None, None,15,7])
    print_tree(tree)