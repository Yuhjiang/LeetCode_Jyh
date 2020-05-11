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
