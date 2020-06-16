# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        parents = {}

        def dfs(node: TreeNode, level: int):
            if node:
                if node.left:
                    parents[node.left.val] = node
                    dfs(node.left, level+1)
                if node.right:
                    parents[node.right.val] = node
                    dfs(node.right, level+1)

        dfs(root, 0)

        p_parents = [p]
        p_val = p.val
        while parents.get(p_val) is not None:
            p_parents.append(parents[p_val])
            p_val = parents[p_val].val
        q_parents = [q]
        q_val = q.val
        while parents.get(q_val) is not None:
            q_parents.append(parents[q_val])
            q_val = parents[q_val].val

        i = 0

        while i < len(p_parents):
            if p_parents[i] in q_parents:
                break
            i += 1
        return p_parents[i]


if __name__ == '__main__':
    from utils import BuildTree
    # tree = BuildTree().buildTree([3, 5, 6, 2, 7, 4, 1, 0, 8],
    #                              [6, 5, 7, 2, 4, 3, 0, 1, 8])
    tree = BuildTree().buildTree([-1, 0, -2, 8, 4, 3],
                                 [8, -2, 0, 4, -1, 3])
    p = tree.left.left.left
    q = tree.left.right
    # q = tree.left.right.right
    print(Solution().lowestCommonAncestor(tree, p, q).val)