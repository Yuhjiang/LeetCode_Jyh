# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        self.convert(root)
        return root

    def convert(self, root):
        """
        反向中序遍历
        :param root: 
        :return:
        """
        if not root:
            return
        self.convert(root.right)
        self.sum += root.val
        root.val = self.sum
        self.convert(root.left)