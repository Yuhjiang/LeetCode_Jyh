# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = head
        if not tmp:
            return tmp

        while tmp.next:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head


if __name__ == '__main__':
    from problems.utils import create_list, print_list
    print_list(
        Solution().deleteDuplicates(
            create_list([1, 1, 2, 3, 3])
        )
    )
    print_list(
        Solution().deleteDuplicates(
            create_list([1,])
        )
    )