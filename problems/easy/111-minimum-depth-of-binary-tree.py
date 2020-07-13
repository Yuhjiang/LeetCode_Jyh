class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        self.min_depth = None

        def pre_order_traversal(tree: TreeNode, depth: int):
            if not tree:
                return None
            if not (tree.left or tree.right):
                if not self.min_depth:
                    self.min_depth = depth
                else:
                    self.min_depth = self.min_depth if self.min_depth < depth else depth
            else:
                pre_order_traversal(tree.left, depth+1)
                pre_order_traversal(tree.right, depth+1)

        pre_order_traversal(root, 1)

        return self.min_depth if self.min_depth is not None else 0


class NewSolution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = [(root, 1)]

        while q:
            t, depth = q.pop(0)

            if not (t.left or t.right):
                return depth
            if t.left:
                q.append((t.left, depth+1))
            if t.right:
                q.append((t.right, depth+1))
        return 0

