from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(list_node):
    while list_node:
        print(list_node.val, end=' -> ')
        list_node = list_node.next
    print('None')


def create_list(nodes):
    if not nodes:
        return None
    t = ListNode(nodes[0])
    temp = t
    for i in nodes:
        temp.next = ListNode(i)
        temp = temp.next
    return t.next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(nodes: List) -> TreeNode:
    t = TreeNode(nodes.pop(0))
    queue = [t]

    while nodes:
        tmp = queue.pop(0)
        left = nodes.pop(0)
        left = TreeNode(left) if left else None
        if not nodes:
            break
        right = nodes.pop(0)
        right = TreeNode(right) if right else None
        tmp.left = left
        tmp.right = right
        if left:
            queue.append(left)
        if right:
            queue.append(right)

    return t


def print_tree(root: TreeNode):
    queue = [root]

    while queue:
        tmp = queue.pop(0)
        if tmp:
            print(tmp.val, end=' ')
        else:
            print(None, end=' ')
            continue

        queue.append(tmp.left)
        queue.append(tmp.right)


class BuildTree:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index = {n: i for i, n in enumerate(inorder)}

        def build(pre_left: int, pre_right: int, in_left: int, in_right: int):
            if pre_left > pre_right or in_left > in_right:
                return None
            root_pos = pre_left

            in_pos = index[preorder[root_pos]]
            length = in_pos - in_left
            root = TreeNode(preorder[root_pos])
            root.left = build(pre_left+1, pre_left+length, in_left, in_pos-1)
            root.right = build(pre_left+length+1, pre_right, in_pos+1, in_right)

            return root

        max_len = len(preorder)
        return build(0, max_len-1, 0, max_len-1)
