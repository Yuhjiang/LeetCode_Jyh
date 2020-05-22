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
            left = q.pop(0)
            right = q.pop(0)
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


class NewSolution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, t1, t2):
        if not (t1 or t2):
            return True
        elif not (t1 and t2):
            return False
        else:
            return t1.val == t2.val and self.is_mirror(t1.left, t2.right) and self.is_mirror(t1.right, t2.left)


class NewQueueSolution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [(root.left, root.right)]

        while queue:
            t1, t2 = queue.pop()
            if (t1 and not t2) or (not t1 and t2):
                return False
            if t1 and t2:
                if t1.val != t2.val:
                    return False
                queue.append((t1.left, t2.right))
                queue.append((t1.right, t2.left))

        return True


if __name__ == '__main__':
    pass