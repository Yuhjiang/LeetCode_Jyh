# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            next_ = head.next
            head.next = prev
            prev = head
            head = next_

        return prev


if __name__ == '__main__':
    from problems.utils import print_list, create_list
    print_list(Solution().reverseList(create_list([1, 2, 3, 4])))
