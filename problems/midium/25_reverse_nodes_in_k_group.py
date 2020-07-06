# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        end = head
        for _ in range(k):
            if not end:
                return head
            end = end.next

        def reverse(root, tail):
            last = None
            while root != tail:
                curr = root
                root = root.next
                curr.next = last
                last = curr
            return last

        result = reverse(head, end)
        head.next = self.reverseKGroup(end, k)

        return result


class NewSolution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy

        while head:
            tail = prev_node.next
            for _ in range(k):
                if not tail:
                    return dummy.next
                tail = tail.next
            _next = tail
            new_head, tail = self.reverse(head, tail)
            prev_node.next = new_head
            tail.next = _next
            prev_node = tail
            head = tail.next

        return dummy.next

    def reverse(self, root, tail):
        last = None
        tmp = root
        while root != tail:
            curr = root
            root = root.next
            curr.next = last
            last = curr
        return last, tmp


if __name__ == '__main__':
    from problems.utils import print_list, create_list
    print_list(NewSolution().reverseKGroup(create_list([1,2,3,4,5]), 2))
    print_list(NewSolution().reverseKGroup(create_list([1,2]), 2))
    print_list(NewSolution().reverseKGroup(create_list([1]), 2))
