# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        fast = head
        if fast.next:
            fast = fast.next
        slow = head

        has_cycle = False
        while fast and fast.next:
            if fast == slow:
                has_cycle = True
                break
            fast = fast.next
            if fast.next:
                fast = fast.next
            slow = slow.next

        if not has_cycle:
            return None
        new = head
        slow = slow.next
        while new != slow:
            slow = slow.next
            new = new.next
        return slow


if __name__ == '__main__':
    n1 = ListNode(3)
    n2 = ListNode(2)
    n1.next = n2
    n2.next = ListNode(0)
    n4 = ListNode(-4)
    n2.next.next = n4
    n4.next = n2

    print(Solution().detectCycle(n1))