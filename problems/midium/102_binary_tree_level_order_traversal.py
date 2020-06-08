from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = list()
        q.append((root, 1))    # 存入节点和层级

        res = []

        while q:
            r, level = q.pop(0)
            if level-1 < len(res):
                res[level-1].append(r.val)
            else:
                res.append([r.val])

            if r.left:
                q.append((r.left, level+1))
            if r.right:
                q.append((r.right, level+1))

        return res


if __name__ == '__main__':
    from utils import create_tree
    # t = create_tree([3, 9, 20, None, None, 15, 7])
    t = create_tree([3, 9, None, None, None])
    print(Solution().levelOrder(t))
