# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def pre_order_traversal(tree: TreeNode, target: int):
            if tree:
                if target < 0:
                    return False
                if tree.val == target and not (tree.left or tree.right):
                    return True

                return pre_order_traversal(tree.left, target-tree.val) or\
                       pre_order_traversal(tree.right, target-tree.val)
            else:
                return False

        return pre_order_traversal(root, sum)


if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(2)
    print(Solution().hasPathSum(t, 1))