# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head or k < 1:
            return None
        slow = fast = head

        for i in range(k):
            if not fast:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow


if __name__ == '__main__':
    from problems.utils import create_list, print_list

    print_list(Solution().getKthFromEnd(create_list([1]), 1))
    print_list(Solution().getKthFromEnd(create_list([1]), 0))
    print_list(Solution().getKthFromEnd(create_list([]), 1))
    print_list(Solution().getKthFromEnd(create_list([1, 2, 3, 4, 5]), 2))
    print_list(Solution().getKthFromEnd(create_list([1, 2, 3, 4, 5]), 5))
