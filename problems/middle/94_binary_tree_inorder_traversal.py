from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
            else:
                return

        dfs(root)
        return res


if __name__ == '__main__':
    from utils import create_tree, print_tree
    t = create_tree([1, None, 2, 3, None, None])
    print(Solution().inorderTraversal(t))
