class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = head
        elems = []

        while temp:
            elems.append(temp.val)
            temp = temp.next

        return elems == elems[::-1]


class SolutionReverseList:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head

        tmp, pre = None, None
        while fast and fast.next:
            fast = fast.next.next
            # 反转链表
            tmp = slow
            slow = slow.next

            tmp.next = pre
            pre = tmp

        if fast:
            slow = slow.next

        while slow and tmp:
            if slow.val != tmp.val:
                return False
            slow = slow.next
            tmp = tmp.next
        return True


if __name__ == '__main__':
    s = SolutionReverseList()
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(1)
    print(s.isPalindrome(node))
