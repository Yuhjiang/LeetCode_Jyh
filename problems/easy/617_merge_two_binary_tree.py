# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        q1 = [t1]
        q2 = [t2]

        new_val = []
        while q1 and q2:
            node1 = q1.pop(0)
            node2 = q2.pop(0)

            val = None
            if node1:
                val = node1.val
            if node2:
                val = node2.val + (val if val else 0)
            if val or val == 0:
                new_val.append(val)
            else:
                new_val.append(None)
            if node1 or node2:
                if node1:
                    q1.append(node1.left)
                    q1.append(node1.right)
                else:
                    q1.append(None)
                    q1.append(None)
                if node2:
                    q2.append(node2.left)
                    q2.append(node2.right)
                else:
                    q2.append(None)
                    q2.append(None)

        if new_val[0] or new_val[0] == 0:
            new_t = TreeNode(new_val[0])
        else:
            new_t = None
        new_val.pop(0)

        nodes = [new_t]

        while nodes and new_val:
            node = nodes.pop(0)
            if not node:
                continue
            left = new_val.pop(0)
            right = new_val.pop(0)
            if left or left == 0:
                node.left = TreeNode(left)
                nodes.append(node.left)
            else:
                nodes.append(None)
            if right or right == 0:
                node.right = TreeNode(right)
                nodes.append(node.right)
            else:
                nodes.append(None)
        return new_t


class RecursionSolution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(tree1, tree2, new_tree):
            if not tree1:
                return tree2
            if not tree2:
                return tree1
            new_tree.val = tree1.val + tree2.val
            new_tree.left = dfs(tree1.left, tree2.left, TreeNode(0))
            new_tree.right = dfs(tree1.right, tree2.right, TreeNode(0))

            return new_tree

        return dfs(t1, t2, TreeNode(0))


class QueueSolution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2:
            return t1 if t1 else t2

        q = [(t1, t2)]
        while q:
            tree1, tree2 = q.pop(0)
            tree1.val += tree2.val

            if tree1.left and tree2.left:
                q.append((tree1.left, tree2.left))
            else:
                tree1.left = tree1.left if tree1.left else tree2.left
            if tree1.right and tree2.right:
                q.append((tree1.right, tree2.right))
            else:
                tree1.right = tree1.right if tree1.right else tree2.right

        return t1


def traversal(t):
    q = [t]
    while q:
        node = q.pop(0)
        print(node.val if node else None, end=' ')
        if node:
            q.append(node.left)
            q.append(node.right)


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.left.left = TreeNode(5)
    t1.right = TreeNode(2)
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.left.right = TreeNode(4)
    t2.right = TreeNode(3)
    t2.right.right = TreeNode(7)

    t = QueueSolution().mergeTrees(t1, t2)
    traversal(t)
    print('\n')

    """
    [3,4,5,1,2,null,null,0]
[4,1,2]
    """
    t1 = TreeNode(3)
    t1.left = TreeNode(4)
    t1.right = TreeNode(5)
    t1.left.left = TreeNode(1)
    t1.left.right = TreeNode(2)
    t1.left.left.left = TreeNode(0)
    t2 = TreeNode(4)
    t2.left = TreeNode(1)
    t2.right = TreeNode(2)
    t = QueueSolution().mergeTrees(t1, t2)
    traversal(t)