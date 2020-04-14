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
