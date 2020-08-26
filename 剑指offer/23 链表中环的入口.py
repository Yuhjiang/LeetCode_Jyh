from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node = self.meeting_node(head)
        if not node:
            return None

        length = 1
        tmp = node
        while tmp.next != node:
            tmp = tmp.next
            length += 1

        fast = head
        for i in range(length):
            fast = fast.next

        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next

        return slow

    def meeting_node(self, head: ListNode) -> Optional[ListNode]:
        if not head:
            return None

        slow = fast = head

        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return None

            if slow == fast:
                return slow

        return None


if __name__ == '__main__':
    from problems.utils import create_list, print_list
    t = create_list([3,2,0,-4])
    t.next.next.next.next = t.next
    print(Solution().detectCycle(t).val)
