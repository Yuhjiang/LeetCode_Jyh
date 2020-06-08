# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.last = None
        self.flatten_(root)

    def flatten_(self, r):
        if r:
            self.flatten_(r.right)
            self.flatten_(r.left)
            r.right = self.last
            r.left = None
            self.last = r
        else:
            return None




if __name__ == '__main__':
    from utils import create_tree, print_tree
    ro = create_tree([1, 2, 5, 3, 4, None, 6, None, None, None, None, None, None])
    Solution().flatten(ro)
    print_tree(ro)