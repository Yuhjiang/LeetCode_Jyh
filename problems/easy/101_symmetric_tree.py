# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left: TreeNode, right: TreeNode) -> bool:
        if not (left or right):
            return True
        elif (left and not right) or (right and not left):
            return False

        if left.val == right.val:
            return self.is_mirror(left.left, right.right) \
                   and self.is_mirror(left.right, right.left)
        else:
            return False


class QueueSolution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = [root, root]

        while q:
            left = q.pop()
            right = q.pop()
            if (left and not right) or (not left and right):
                return False
            if not (left or right):
                continue
            if left.val != right.val:
                return False
            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.right)
        return True


if __name__ == '__main__':
    pass