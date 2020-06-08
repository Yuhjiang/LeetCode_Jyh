# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import math

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def dfs(root, lower=-math.inf, upper=math.inf):
            if not root:
                return True
            else:
                if not dfs(root.left, lower, root.val):
                    return False
                if not dfs(root.right, root.val, upper):
                    return False
                if not lower < root.val < upper:
                    return False
                else:
                    return True

        return dfs(root)


if __name__ == '__main__':
    from utils import create_tree
    # root = create_tree([10, 5, 15, None, None, 6, 20])
    root = TreeNode(1)
    root.left = TreeNode(1)
    print(Solution().isValidBST(root))