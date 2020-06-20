# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        pos = length - n
        cur = 0
        temp = head

        if pos == 0:
            return head.next
        while temp:
            cur += 1
            if cur == pos:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head


class NewSolution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        slow = head
        while fast.next:
            print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    from problems.utils import create_list, print_list
    l = create_list([1, 2, 3, 4, 5])
    print_list(NewSolution().removeNthFromEnd(l, 5))
    pass