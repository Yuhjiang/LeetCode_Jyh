class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        length = 0
        tmp = head
        last = None

        while tmp:
            length += 1
            last = tmp
            tmp = tmp.next

        pos = length - k % length    # 只需一次遍历的位置
        if pos == length:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        tmp = dummy
        while pos > 0:
            tmp = tmp.next
            pos -= 1
        ans = tmp.next
        tmp.next = None
        last.next = head

        return ans


if __name__ == '__main__':
    from problems.utils import create_list, print_list
    print_list(Solution().rotateRight(create_list([1, 2, 3, 4, 5]), 2))
    print_list(Solution().rotateRight(create_list([]), 1))
