from problems.utils import create_list, print_list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        temp = res

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next

        if l1:
            temp.next = l1
        if l2:
            temp.next = l2

        return res.next


if __name__ == '__main__':
    l1 = create_list([1, 2, 4])
    l2 = create_list([1, 3, 4])
    print_list(Solution().mergeTwoLists(l1, l2))
