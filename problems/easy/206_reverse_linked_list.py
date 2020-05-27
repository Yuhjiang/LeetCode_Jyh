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


class NewSolution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            curr = head
            head = head.next
            curr.next = last
            last = curr
        return last


if __name__ == '__main__':
    from utils import print_list, create_list
    head = create_list([1, 2, 3, 4, 5])

    s = NewSolution()
    print_list(s.reverseList(head))
