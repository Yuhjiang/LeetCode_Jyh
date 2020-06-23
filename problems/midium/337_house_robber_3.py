# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        memo = {}

        def dfs(node):
            if node in memo:
                return memo[node]
            if not node:
                return 0
            elif not node.left and not node.right:
                memo[node] = node.val
                return node.val
            else:
                memo[node] = 0
                left = node.left
                right = node.right
                if left and not right:
                    memo[node] = max(node.val + dfs(left.left) + dfs(left.right),
                                     dfs(left))
                elif right and not left:
                    memo[node] = max(node.val + dfs(right.left) + dfs(right.right),
                                     dfs(right))
                else:
                    memo[node] = max(node.val + dfs(left.left) + dfs(left.right)
                                     + dfs(right.left) + dfs(right.right),
                                     dfs(left) + dfs(right))
                return memo[node]

        res = dfs(root)
        return res


if __name__ == '__main__':
    # tree = TreeNode(3)
    # tree.left = TreeNode(2)
    # tree.left.right = TreeNode(3)
    # tree.right = TreeNode(3)
    # tree.right.right = TreeNode(1)
    tree = TreeNode(3)
    # tree.left = TreeNode(4)
    # tree.right = TreeNode(5)
    # tree.left.left = TreeNode(1)
    # tree.left.right = TreeNode(3)
    # tree.right.right = TreeNode(1)

    print(Solution().rob(tree))