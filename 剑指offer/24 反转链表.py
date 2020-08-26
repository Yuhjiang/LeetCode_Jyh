
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev


if __name__ == '__main__':
    from problems.utils import create_list, print_list
    print_list(Solution().reverseList(create_list([1, 2, 3, 4, 5])))
    print_list(Solution().reverseList(create_list([1])))