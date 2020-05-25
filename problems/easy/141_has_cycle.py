# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head.next
        fast = head.next
        if fast:
            fast = fast.next
        else:
            return False
        while fast:
            if fast.val == slow.val:
                return True
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return False

        return False


class NewSolution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        if not fast or not fast.next:
            return False
        else:
            fast = fast.next.next
        slow = head.next

        while slow or fast:
            if fast == slow:
                return True
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
        return False


if __name__ == '__main__':
    from utils import create_list, print_tree
    create_list([3,2,0,-4])