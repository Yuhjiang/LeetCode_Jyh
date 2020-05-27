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
