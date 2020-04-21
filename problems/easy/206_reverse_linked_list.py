# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = head
        first = new_head

        temp = head.next

        while temp:
            t = temp.next
            temp.next = new_head
            new_head = temp
            temp = t

        first.next = None

        return new_head


def print_list(node):
    while node:
        print(node.val, end=' ')
        node = node.next


if __name__ == '__main__':
    head = ListNode(1)
    temp = head
    for i in [2, 3, 4, 5]:
        temp.next = ListNode(i)
        temp = temp.next

    s = Solution()
    print_list(s.reverseList(head))
