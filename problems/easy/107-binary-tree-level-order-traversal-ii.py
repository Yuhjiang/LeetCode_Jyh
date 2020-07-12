from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        q = list()
        if not root:
            return []

        level = 0
        q.append((root, level))
        ans = []

        while q:
            tmp = q.pop(0)
            if tmp[1] >= len(ans):
                ans.append([tmp[0].val])
            else:
                ans[tmp[1]].append(tmp[0].val)

            if tmp[0].left:
                q.append((tmp[0].left, tmp[1]+1))
            if tmp[0].right:
                q.append((tmp[0].right, tmp[1]+1))

        return ans[::-1]


if __name__ == '__main__':
    from problems.utils import BuildTree
    tree = BuildTree().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(Solution().levelOrderBottom(tree))