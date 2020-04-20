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


if __name__ == '__main__':
    s = Solution()
    # s.hasCycle()