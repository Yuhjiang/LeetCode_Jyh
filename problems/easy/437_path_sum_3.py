from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        exists_sum = {0: 1}     # 存储了遍历某个节点前所有可能的和
        self.count = 0
        current_sum = 0

        self.dfs(root, sum, current_sum, exists_sum)

        return self.count

    def dfs(self, root, sum, current_sum, exists_sum):
        if not root:
            return 0
        current_sum += root.val
        # 查找已有的和是否可以减去得到我们的目标和sum
        if current_sum - sum in exists_sum:
            self.count += exists_sum[current_sum-sum]
        # 保存当前的和的情况
        exists_sum[current_sum] = exists_sum.get(current_sum, 0) + 1

        if root.left:
            self.dfs(root.left, sum, current_sum, exists_sum)
        if root.right:
            self.dfs(root.right, sum, current_sum, exists_sum)

        # 还原现场
        exists_sum[current_sum] -= 1


class NewSolution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.memo = defaultdict(int)
        self.memo[0] = 1
        self.count = 0
        last = 0

        self.dfs(root, sum, last)
        return self.count

    def dfs(self, root: TreeNode, sum: int, last):
        if not root:
            return None
        last += root.val
        if last - sum in self.memo:
            self.count += self.memo[last-sum]
        self.memo[last] += 1

        self.dfs(root.left, sum, last)
        self.dfs(root.right, sum, last)
        self.memo[last] -= 1


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(2)
    root.left.right.right = TreeNode(1)
    root.right.right = TreeNode(11)
    s = NewSolution()
    print(s.pathSum(root, 8))