# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            next_ = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = next_
            pre = tail
            head = tail.next
        return dummy.next

    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head

        while prev != tail:
            next_ = p.next
            p.next = prev
            prev = p
            p = next_

        return tail, head


if __name__ == '__main__':
    from problems.utils import create_list, print_list

    print_list(Solution().reverseKGroup(create_list([1, 2]), 2))
