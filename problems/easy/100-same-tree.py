class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def preorder_traversal(tree1: TreeNode, tree2: TreeNode):
            if not tree1 and not tree2:
                return True
            if (tree1 and not tree2) or (not tree1 and tree2):
                return False

            return tree1.val == tree2.val and \
                   preorder_traversal(tree1.left, tree2.left) and \
                   preorder_traversal(tree1.right, tree2.right)

        return preorder_traversal(p, q)



