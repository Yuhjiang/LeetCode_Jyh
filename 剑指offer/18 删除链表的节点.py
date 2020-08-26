# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next

        tmp = head
        while tmp:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
                break

            tmp = tmp.next
        return head
